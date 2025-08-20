from sqlalchemy.orm import sessionmaker
from models import Author , Book , Member , engine
from sqlalchemy import select

Session = sessionmaker(bind=engine)


def add_author(name : str , birth_year : int | None = None) :
    with Session() as session :
        try:
            new_author = Author(name = name , birth_year = birth_year)

            session.add(new_author)

            session.commit()

            print(f"Author '{name}' added successfully.")
        except ValueError as err:
            print(f"The error is : {err=} .")
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

def add_book(title: str, isbn: str, author_id: int) :
    with Session() as session :
        try:
            new_book = Book(title = title , isbn = isbn , author_id = author_id)

            session.add(new_book)

            session.commit()

            print(f"Book '{title}' added successfully.")
        except ValueError as err:
            print(f'The error is : {err=}')
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}") 

def add_member(name: str, membership_id: str):
    with Session() as session :
        try:
            new_member = Member(name = name , membership_id = membership_id)

            session.add(new_member)

            session.commit()

            print(f"Member '{name}' added successfully.")
        except ValueError as err:
            print(f"The error is : {err=}")
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

def get_all_authors() -> list[Author] :
    list_author = []
    with Session() as session :
        try:
            list_author = session.execute(select(Author)).scalars().all()
            print("Take authors is Successfully.")
        except Exception as err:
          print(f'An exception occurred {err=}.')
    return list_author

def get_all_books() -> list[Book] :
    list_book = []
    with Session() as session :
        try:
            list_book = session.execute(select(Book)).scalars().all()
            print("Take Book is Successfully.")
        except Exception as err:
            print(f'An exception occurred {err=}.')
    return list_book

def get_all_members() -> list[Member] :
    list_member = []
    with Session() as session :
        try:
            list_member = session.execute(select(Member)).scalars().all()
            print("Take Members is Successfully.")
        except Exception as err:
          print(f'An exception occurred {err=}.')
    return list_member

def find_author_by_id(author_id: int) -> Author | None :
    author = None
    with Session() as session :
        try:
            author = session.get(Author , author_id)
            print(f"The author with {author_id=} Find.")
        except Exception as err:
            print(f"An exception occurred {err=}.")
    return author

def find_book_by_isbn(isbn: str) -> Book | None :
    book = None
    with Session() as session :
        try:
            stmt = select(Book).where(Book.isbn == isbn)
            book = session.execute(stmt).scalars().first()
            print(f"The book with {isbn=} Find.")
        except Exception as err:
          print(f'An exception occurred {err=}.')
    return book

def find_member_by_membership_id(membership_id: str) -> Member | None :
    member = None
    with Session() as session : 
        try:
            stmt = select(Member).where(Member.membership_id == membership_id)
            member = session.execute(stmt).scalars().first()
            print(f"The member with {membership_id=} Find.")
        except Exception as err:
            print(f'An exception occurred {err=}.')
    return member