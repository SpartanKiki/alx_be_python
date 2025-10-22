def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    # Create an empty shopping list
    shopping_list = []

    # Infinite loop until user chooses to exit
    while True:
        display_menu()  # Show menu options each time
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.\n")

        elif choice == '2':
            # Remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.\n")
            else:
                print(f"'{item}' not found in the shopping list.\n")

        elif choice == '3':
            # View the shopping list
            if len(shopping_list) == 0:
                print("Your shopping list is empty.\n")
            else:
                print("Your Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
                print()

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid input
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
