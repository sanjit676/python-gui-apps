def show_menu():
    print("\nContact Book Menu:")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Remove Contact")
    print("4. Exit")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts available!")
    else:
        print("\nContacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

def add_contact(contacts):
    name = input("\nEnter contact name: ").strip()
    number = input("Enter contact number: ").strip()
    if name and number:
        contacts[name] = number
        print(f"Contact '{name}' added.")
    else:
        print("Name and number cannot be empty!")

def remove_contact(contacts):
    name = input("\nEnter the name of the contact to remove: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' removed.")
    else:
        print("Contact not found!")

def main():
    contacts = {}
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            remove_contact(contacts)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
