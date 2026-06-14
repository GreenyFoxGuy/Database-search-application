from Database import Database


def print_menu():
    op_find_town, op_towns_in_district, op_district_list, op_district_stats, op_end = 1, 2, 3, 4, 0
    user_options = ["1 - Hledat obec",
                    "2 - Obce v okrese",
                    "3 - Seznam okresů",
                    "4 - Statistiky okresu",
                    "0 - Ukončit",]
    print("="*20+"\nDemografie ČR\n"+"="*20)
    print("\n".join(user_options))

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
            phrase_to_search = input("Hledat obec: ")
            print(f"Vyhledávání pro {phrase_to_search}:")
            try:
                data = Database().search_town(phrase_to_search)
            except IndexError:
                print("Nebyla nalezena žádná obec.")
                continue

            for town in data:
                print(town)

if __name__ == '__main__':
    main()