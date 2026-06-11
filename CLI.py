from Database import Database

def print_separators():
    print("-"*20)

def print_menu():
    user_options = ["1 - Vyhledat obci",
                    "2 - Vypsat obce v okresu",
                    "3 - Ukončit",]
    print_separators()
    print("\n".join(user_options))
    print_separators()

def main():
    while True:
        print_menu()
        try:
            chosen_option = int(input("Vyberte možnost: "))
        except ValueError:
            print("Please choose a valid option!")
            continue
        if not 1 <= chosen_option <= 3:
            print("Please choose a valid option!")
            continue

        if chosen_option == 1:
            phrase_to_search = input("Vyhledat obci: ")
            print_separators()
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