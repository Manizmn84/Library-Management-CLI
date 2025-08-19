import os
from sqlalchemy import create_engine
from models import Base , engine


if __name__ == "__main__" :
    Base.metadata.create_all(engine)

    print("The Table Create Successfully")