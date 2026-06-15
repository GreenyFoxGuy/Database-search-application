from Database import Database

op_find_town, op_towns_in_district, op_list_districts, op_district_information, op_end = 1, 2, 3, 4, 0

def print_menu():
    user_options = ["1 - Hledat obec",
                    "2 - Obce v okrese",
                    "3 - Seznam okresů",
                    "4 - Statistiky okresu",
                    "0 - Ukončit",]
    print("="*20+"\nDemografie ČR\n"+"="*20+"\n")
    print("\n".join(user_options))

def print_data(data):

    print("\n")
    for row in data:
        print(sub_data)
    print("\n")

def find_town():

    phrase_to_search = input("Hledat obec: ")
    print(f"Vyhledávání pro {phrase_to_search}:")

    try:
        data = Database().search_town(phrase_to_search)
    except IndexError:
        print("Nebyla nalezena žádná obec.")
        return
    
    print_data(data)

def towns_in_district():

    district_id = input("Zadejte ID okresu: ")

    try:
        data = Database().get_district_info(district_id)
    except IndexError:
        print("Nebyl nalezen žádný okres.")
        return

    print_data(data)

def list_districts():

    try:
        data = Database().get_districts()
    except IndexError:
        print("Nebyl nalezen žádný okres.")
        return

    print_data(data)

def district_information():

    district_id = input("Zadejte ID okresu: ")

    try:
        data = Database().get_district_mean_info(district_id)
    except IndexError:
        print("Nebyl nalezen žádný okres.")
        continue

    print(f"\nPočet obyvatel: {data[0]}\nPrůměrný věk: {data[1]}\nPoměr muži/ženy: {data[2]} / {data[3]}\n")

def main():

    while True:
        print_menu()
        try:
            chosen_option = int(input("Vyberte možnost: "))
        except ValueError:
            print("Please choose a valid option!")
            continue
        if not 0 <= chosen_option <= 4:
            print("Please choose a valid option!")
            continue

        if chosen_option == op_find_town:
            find_town()

        if chosen_option == op_towns_in_district:
            towns_in_district()

        if chosen_option == op_list_districts:
            list_districts()

        if chosen_option == op_district_information:
            district_information()

        if chosen_option == op_end:
            break

if __name__ == '__main__':
    main()