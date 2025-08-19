# Library Management System

A simple, terminal-based Library Management System built with Python using Object-Oriented Programming (OOP) principles. This project allows users to manage books, authors, and library members through a command-line interface, with all data saved to a SQLite database.

---

## Features

-   **Manage Books**: Add new books, view all books, and search for specific titles.
-   **Manage Authors**: Add new authors and view all authors.
-   **Manage Members**: Register new library members and view the list of all members.
-   **Borrow & Return**: Handle the process of borrowing a book by a member and returning it.
-   **Data Persistence**: All information is stored in a local SQLite database (`library.db`).

---

## Project Structure
library_project/
│
├── main.py         # Main script to run the application and display the menu.
├── models.py       # Contains the class definitions for Book, Author, and Member.
├── database.py     # Handles all database connections and CRUD operations.
├── controller.py   # Contains the core application logic.
└── README.md       # Project documentation.

---

## Installation and Usage

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-link>
    cd library_project
    ```

2.  **Run the application:**
    (No external libraries are needed if you are using the standard `sqlite3` library)
    ```sh
    python main.py
    ```

3.  **Follow the on-screen menu** to interact with the library system. The database file `library.db` will be created automatically in the project directory on the first run.