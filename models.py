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
        if not name :
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
