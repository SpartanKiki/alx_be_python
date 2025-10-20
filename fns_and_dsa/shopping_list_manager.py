def display_menu():
    """This function just shows the options to the user."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # This is our empty shopping list at the start
    shopping_list = []

    # Loop forever until the user decides to exit
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # 1️⃣ Add an item
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"✅ '{item}' has been added to the list.")

        elif choice == '2':
            # 2️⃣ Remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"🗑️ '{item}' has been removed.")
            else:
                print(f"⚠️ '{item}' not found in the list.")

        elif choice == '3':
            # 3️⃣ View the list
            if len(shopping_list) == 0:
                print("🛍️ The shopping list is empty.")
            else:
                print("📝 Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")

        elif choice == '4':
            # 4️⃣ Exit
            print("👋 Goodbye!")
            break

        else:
            # Invalid input handling
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
