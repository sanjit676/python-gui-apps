def show_menu():
    print("\nLibrary Menu:")
    print("1. View Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Exit")

def view_books(library):
    if not library:
        print("\nNo books in the library!")
    else:
        print("\nBooks in the Library:")
        for i, book in enumerate(library, 1):
            print(f"{i}. {book}")

def add_book(library):
    book = input("\nEnter the name of the book to add: ").strip()
    if book:
        library.append(book)
        print(f"Book '{book}' added to the library.")
    else:
        print("Book name cannot be empty!")

def remove_book(library):
    try:
        book_number = int(input("\nEnter the book number to remove: "))
        if 1 <= book_number <= len(library):
            removed_book = library.pop(book_number - 1)
            print(f"Book '{removed_book}' removed from the library.")
        else:
            print("Invalid book number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    library = []
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            view_books(library)
        elif choice == "2":
            add_book(library)
        elif choice == "3":
            remove_book(library)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
