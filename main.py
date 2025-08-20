from models import engine, Base
from controller import LibraryController

def main_menu():
    controller = LibraryController()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add New Author")
        print("2. Add New Book")
        print("3. Add New Member")
        print("---------------------------------")
        print("4. Display All Authors")
        print("5. Display All Books")
        print("6. Display All Members")
        print("---------------------------------")
        print("7. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == '1':
            controller.add_new_author()
        elif choice == '2':
            controller.add_new_book()
        elif choice == '3':
            controller.add_new_member()
        elif choice == '4':
            controller.display_all_authors()
        elif choice == '5':
            controller.display_all_books()
        elif choice == '6':
            print("Display all members feature is not implemented yet.")
        elif choice == '7':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    
    main_menu()