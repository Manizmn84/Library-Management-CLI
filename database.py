from sqlalchemy.orm import sessionmaker
from models import Author , Book , Member , engine

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
