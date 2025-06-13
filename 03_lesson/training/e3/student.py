class Student:

    def __init__(self, _name, _surname, _age, _course):
        self.name = _name
        self.surname = _surname
        self.age = _age
        self.course = _course

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} лет, " \
               f"курс: {self.course}"
