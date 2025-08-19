import os
from sqlalchemy import create_engine
from models import Base


if __name__ == "__main__" :
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "library.db")
    engine = create_engine(f"sqlite:///{db_path}")

    Base.metadata.create_all(engine)

    print("The Table Create Successfully")