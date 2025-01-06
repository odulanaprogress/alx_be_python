def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty list
    while True:
        display_menu()  # Show the menu
        choice = input("Enter your choice: ").strip()  # Get user input

        if choice == '1':  # Add item
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)  # Append the item to the list
            print(f"'{item}' has been added to your shopping list.")
        elif choice == '2':  # Remove item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")
        elif choice == '3':  # View list
            if shopping_list:
                print("\nYour Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == '4':  # Exit
            print("Goodbye!")
            break
        else:  # Invalid input
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()
