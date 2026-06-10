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
        query = 'SELECT okresy.nazev, obce_pob.nazev, obce_pob.pocet_obyvatel, obce_pob.prumerny_vek FROM okresy JOIN obce_pob ON obce_pob.id_okres = okresy.id_okres WHERE okresy.id_okres = %s'
        cur.execute(query, (user_input,))
        rows = cur.fetchall()
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
        for row in data:
            reformated_row = row[1] + " | " + str(row[2]) + " | " + str(row[3])
            reformated_data.append(reformated_row)
    if option == "1":
        for town in data:
            reformated_data.append(town[0])
        district = ""

    return reformated_data, district


def print_data(data, district, option, town):

    if option == "1":
        print(f"Vyhledávání pro {town}:")
    elif option == "2":
        print("-"*5 + district + "-"*5)

    for row in data:
        print(row)
    print("-"*15)
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
        if show_options != "A" or show_options != "N":
            print("Please choose a valid option!")
            return False
        data, town = search_in_db(show_options, option)
        if show_options == "A":
            district = ""
        else:
            data, district = reformate_data(data, option)
        print_data(data, district, option, town)
    elif option == "1":
        data, town = search_in_db("N", option)
        data, district = reformate_data(data, option)
        print_data(data, "", option, town)

    return False
if __name__ == "__main__":
    while True:
        end = main()
        if end:
            break

