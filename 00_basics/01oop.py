# =========== TYPE HINTING ==============
from typing import List


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Books: {self.name}"


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."


l = [12, 15.7, -9.54]
print(list_avg((1, 2, 5)))


# # =========== CLASS COMPOSITION ==============
# class BookShelf:
#     def __init__(self, *books):
#         self.books = books

#     def __str__(self) -> str:
#         return f"Bookshelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Books: {self.name}"


# book1 = Book("Harry Potter")
# book2 = Book("Python 101")
# shelf = BookShelf(book1, book2)
# print(shelf)


# # =========== CLASS INHERITANCE ==============
# class Device:
#     def __init__(self, name, connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected = True

#     def __str__(self):
#         return f"Device {self.name!r} ({self.connected_by})"

#     def disconnect(self):
#         self.connected = False
#         print(f"{self.name} disconnected.")


# class Printer(Device):
#     def __init__(self, name, connected_by, capacity):
#         super().__init__(name, connected_by)
#         self.capacity = capacity
#         self.remaining_pages = capacity

#     def __str__(self):
#         return f"{super().__str__()} ({self.remaining_pages!r} pages remaining.)"

#     def print(self, pages):
#         if not self.connected:
#             print("Your printer is not connected!")
#             return
#         print(f"Printed {pages}.")
#         self.remaining_pages -= pages


# printer = Printer("Printer", "USB", 500)
# print(printer)
# printer.print(20)
# print(printer)
# printer.disconnect()
# print(printer)
# printer.print(20)


## classmethod, staticmethod
# class ClassTest:
#     def instance_method(self):
#         print(f"Called instance method of: {self}")

#     @classmethod
#     def class_method(cls):
#         print("Called class method of:", {cls})

#     @staticmethod
#     def static_method():
#         print("Called static method:")


# test = ClassTest()
# test.instance_method()
# ClassTest.instance_method(test)
# ClassTest.class_method()
# ClassTest.static_method()


# # OOP: Magic methods __str__ and __repr__
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Person {self.name}, {self.age} yo."
#     def __repr__(self):
#         return f"<Person {self.name}, {self.age}>."
# bob = Person("Bob", 35)
# print(bob)
# print(str(bob))
## 001 OOP
# class Student:
#     def __init__(self, name, grades=()):
#         self.name = name
#         self.grades = grades
#     def average_grade(self):
#         return sum(self.grades)/len(self.grades)

# rolf = Student("Rolf", (90, 90, 93, 78, 90))
# print(f"Rolf's average grade: {rolf.average_grade()}")
