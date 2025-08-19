class Author:
    def __init__(self , id: int | None = None , name: str , birth_year: int | None = None):
        self.id = id
        self.name = name
        self.birth_year = birth_year
    
    @property
    def name(self) -> str :
        return self._name

    @name.setter
    def name(self , name: str):
        if not name or not name.strip() :
            raise ValueError("The Name is Null")
        if not isinstance(name , str) :
            raise ValueError("The Name is not Type of Str")
        self._name = name

    @property
    def birth_year(self) -> int | None:
            return self._birth_year
    
    @birth_year.setter
    def birth_year(self , birth_year: int):
        if birth_year is not None and not isinstance(birth_year, int):
            raise ValueError("The Birth Year is Type is Invalid")
        self._birth_year = birth_year

    def __str__(self):
        if self._birth_year:
            return f"Author(ID: {self.id}, Name: {self.name}, Birth Year: {self.birth_year})"
        return f"Author(ID: {self.id}, Name: {self.name})"


class Book:
    def __init__(self , id: int | None = None , title: str , isbn: str , author_id: int , is_borrowed: bool = False):
        self.id = id 
        self.title = title
        self.isbn = isbn
        self.author_id = author_id
        self.is_borrowed = is_borrowed
    
    @property
    def title(self) -> str :
        return self._title
    
    @title.setter
    def title(self , title) :
        if not isinstance(title , str) or not title.strip() :
            raise ValueError("The Title is Not Str")
        self._title = title
    
    @property
    def isbn(self) -> str :
        return self._isbn

    @isbn.setter
    def isbn(self , isbn):
        if not isinstance(isbn , str) or not isbn.strip() :
            raise ValueError("The isbn is Invalid")
        self._isbn = isbn
    
    @property
    def author_id(self) -> int:
        return self._author_id
    
    @author_id.setter
    def author_id(self , id) :
        if not isinstance(id , int) :
            raise ValueError("The author id Should be int Type")
        self._author_id = id

    @property
    def is_borrowed(self) -> bool :
        return self._is_borrowed
    
    @is_borrowed.setter
    def is_borrowed(self , is_borrowed):
        if not isinstance(is_borrowed , bool) :
            raise ValueError("The borrowed Type Should be bool")
        self._is_borrowed = is_borrowed

    def __str__(self):
        return f"Book(ID : {self.id} , Title : {self.title} , Isbn : {self.isbn} , Author_id : {self.author_id} , Is_borrowed : {self.is_borrowed})"
    
class Member:
    def __init__(self , id : int | None = None , name : str , membership_id : str):
        self.id = id
        self.name = name
        self.membership_id = membership_id
    
    @property
    def name(self) -> str :
        return self._name
    
    @name.setter
    def name(self , name) :
        if not isinstance(name  , str) or not name.strip() :
            raise ValueError("The Type of Name is Invalid")
        self._name = name
    
    @property
    def membership_id(self) -> str :
        return self._membership_id
    
    @membership_id.setter
    def membership_id(self , membership_id) :
        if not isinstance(membership_id , str) or not membership_id.strip(): 
            raise ValueError("The membership_id Type is Invalid")
        self._membership_id = membership_id

    def __str__(self):
        return f"Member(ID : {self.id} , Name : {self.name} , Membership_id : {self.membership_id})"