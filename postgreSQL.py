import psycopg


def connect_to_db():

    try:
        conn = psycopg.connect(host="192.168.135.10",
                               port="5432",
                               dbname="obce",
                               user="student",
                               password="bluemonkey3")
        cur = conn.cursor()
    except psycopg.OperationalError as e:
        print(e)
        return None

    return cur, conn

def search_in_db(show_options, option):

    cur, conn = connect_to_db()
    if option == "1":
        town = input("Vyhledat obci: ")
        search_term = f"%{town}%"
        query = 'SELECT obce_pob.nazev FROM obce_pob WHERE obce_pob.nazev ILIKE %s'
        cur.execute(query, (search_term,))
        rows = cur.fetchall()

    elif show_options == "A":
        cur.execute("SELECT * FROM okresy")
        rows = cur.fetchall()
        town = ""

    elif show_options == "N":
        user_input = input("Zadejte kód okresu: ")
        query = """
                SELECT
                    okresy.nazev AS okres,
                    obce_pob.nazev AS obec,
                    obce_pob.pocet_obyvatel,
                    obce_pob.prumerny_vek,
                    SUM(obce_pob.pocet_obyvatel) OVER () AS okres_obyvatel,
                    AVG(obce_pob.prumerny_vek) OVER () AS okres_prumerny_vek,
                    SUM(obce_pob.pocet_muzi) OVER () AS okres_muzi,
                    SUM(obce_pob.pocet_zeny) OVER () AS okres_zeny
                FROM okresy
                JOIN obce_pob
                    ON obce_pob.id_okres = okresy.id_okres
                WHERE okresy.id_okres = %s;
                """
        cur.execute(query, (user_input,))
        rows = cur.fetchall()
        print(rows[0])
        town = ""

    return rows, town

def reformate_data(data, option):
    if not data:
        print("Nebyl nalezen žádný okres.")
        print("-"*15)
        main()

    reformated_data = []
    if option == "2":
        district = data[0][0]
        sum_population = data[0][4]
        mean_age = data[0][5]
        sum_men = data[0][6]
        sum_women = data[0][7]
        for row in data:
            reformated_row = row[1] + " | " + str(row[2]) + " | " + str(row[3])
            reformated_data.append(reformated_row)

        return reformated_data, district, sum_population, mean_age, sum_men, sum_women

    if option == "1":
        for town in data:
            reformated_data.append(town[0])

        return reformated_data, "", "", "", "", ""


def print_data(data, district, option, town, sum_population=None, mean_age=None, sum_men=None, sum_women=None):

    if option == "1":
        print(f"Vyhledávání pro {town}:")
    elif option == "2":
        print("-"*5 + district + "-"*5)

    for row in data:
        print(row)
    print("-"*15)

    if option == "2":
        print("Total population: ", sum_population)
        print("Mean age: ", mean_age)
        print("Men to women ration: ", sum_men, "/", sum_women)
    return 0

def main():

    print("1 - Vyhledat obci\n2 - Vypsat obce v okresu\n3 - Ukončit")
    option = input("Vyberte možnost: ")
    if not option.isdigit() or not 1 <= int(option) <= 3:
        print("Please choose a valid option!")
        return False
    if option == "3":
        return True
    elif option == "2":
        show_options = input("Zobrazit okresy? [A/N]:")
        if show_options != "A" and show_options != "N":
            print("Please choose a valid option!")
            return False
        data, town = search_in_db(show_options, option)
        if show_options == "A":
            district = ""
        else:
            data, district, sum_population, mean_age, sum_men, sum_women = reformate_data(data, option)
        print_data(data, district, option, town, sum_population, mean_age, sum_men, sum_women)
    elif option == "1":
        data, town = search_in_db("N", option)
        data, district, n, o, p, e = reformate_data(data, option)
        print_data(data, "", option, town)

    return False
if __name__ == "__main__":
    while True:
        end = main()
        if end:
            break

