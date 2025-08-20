import os
from sqlalchemy import create_engine, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, validates
from typing import List


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "library.db")
engine = create_engine(f"sqlite:///{db_path}")

class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_year: Mapped[int] = mapped_column(nullable=True)

    books: Mapped[List["Book"]] = relationship(back_populates="author", cascade="all, delete-orphan")

    @validates("name")
    def validate_name(self, key, name_value):
        if not isinstance(name_value, str) or not name_value.strip():
            raise ValueError("Name cannot be empty and must be a string.")
        return name_value.strip()

    def __str__(self):
        return f"Author(ID: {self.id}, Name: '{self.name}')"


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    isbn: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    is_borrowed: Mapped[bool] = mapped_column(default=False)

    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), nullable=False)
    author: Mapped["Author"] = relationship(back_populates="books")

    @validates("title", "isbn")
    def validate_string_fields(self, key, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{key.capitalize()} cannot be empty and must be a string.")
        return value.strip()

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book(ID: {self.id}, Title: '{self.title}', Status: {status})"


class Member(Base):
    __tablename__ = "members"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    membership_id: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    @validates("name", "membership_id")
    def validate_string_fields(self, key, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{key.replace('_', ' ').capitalize()} cannot be empty and must be a string.")
        return value.strip()

    def __str__(self):
        return f"Member(ID: {self.id}, Name: '{self.name}', Membership ID: '{self.membership_id}')"
