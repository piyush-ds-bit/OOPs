# Inheritance lets a class inherit properties and methods from another class.It’s an “is-a” relationship.
# Encourages reuse and extension of existing code.

class User:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "User"

class Student(User):  # Inherits from User
    def get_role(self):
        return "Student"

class Teacher(User):  # Inherits from User
    def get_role(self):
        return "Teacher"
