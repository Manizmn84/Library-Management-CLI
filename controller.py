import database

class LibraryController:
    def __init__(self):
        print("Library Controller Initialized.")
    
    def add_new_author(self) -> None:
        print("\n\t======= Add New Author =======\t")
        name = input("Enter Your Name : ")
        Birth_year = None
        try:
            Birth_year = int(input("Enter Your Birth year :(if don`t want Enter string or nothing) "))
        except:
          print('you don`t want to give the birthday')
        
        database.add_author(name=name , birth_year=Birth_year)

    def add_new_book(self) -> None:
        List_author = database.get_all_authors()
        if not List_author:
            print("We don`t have Author.")
            return 
        print("\n\t======= Add New Book =======\t")
        title = input("Enter The Book title : ")
        isbn = input("Enter The isbn : ")

        author_id = None
        print("Available Authors:")
        for author in List_author :
            print(f"ID: {author.id}, Name: {author.name}")
        
        try:
            author_id = int(input("Enter The author_id : "))
        except ValueError:
            print('Can`t Convert Author Id To int.')
            return
        
        database.add_book(title=title , isbn=isbn , author_id=author_id)
    
    def add_new_member(self) -> None:
        print("\n\t======= Add New Member =======\t")
        name = input("Enter Your Name : ")
        membership_id = input("Enter Membership Id : ")
        
        database.add_member(name=name , membership_id=membership_id)

    def display_all_authors(self) -> None :
        List_author = database.get_all_authors()
        if not List_author :
            print("The Library Don`t have any Author.")
            return

        print("\n\t======= List Author =======\t")
        for author in List_author :
            print(author)

    def display_all_books(self) -> None :
        List_book = database.get_all_books()
        if not List_book :
            print("The Library Don`t have any Book.")
            return

        print("\n\t======= List Book =======\t")
        for book in List_book :
            print(book)
