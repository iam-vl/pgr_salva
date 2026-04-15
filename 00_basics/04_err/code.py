# CUSTOM ERROR CLASSES ##########

book_repr = "<Book {}, read {} pages out of {}>"
total_read_pages_templ = "You have now read {} out of {}."
too_many_pages_read_templ = (
    "You tried to read more pages than the book has: {} vs {} total."
)


# Have to inherit from Error or Exception
class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return book_repr.format(self.name, self.pages_read, self.page_count)

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                too_many_pages_read_templ.format(self.pages_read, self.page_count)
            )
        self.pages_read += pages
        print(total_read_pages_templ.format(self.pages_read, self.page_count))


def runner():
    book = Book("Python 101", 50)
    book.read(35)
    print(book)
    book.read(40)
    print(book)


### ERRORS 1 ################
# book_repr = "<Book {}, read {} pages out of {}>"
# too_many_pages_read_templ = (
#     "You tried to read more pages than the book has {} vs {} total."
# )

# def divide(divider, divisor):
#     # if divisor == 0:
#     #     print("Divisor cannot be 0")
#     #     return
#     if divisor == 0:
#         raise ZeroDivisionError("ERROR: Divisor cannot be 0.")
#     return divider / divisor


# students = [
#     {"name": "Bob", "grades": [75, 90]},
#     {"name": "Rolf", "grades": []},
#     {"name": "Jen", "grades": [100, 90]},
# ]

# try:
#     for st in students:
#         name = st["name"]
#         grades = st["grades"]
#         average = divide(sum(grades), len(grades))
#         print(f"{name} averaged {average}.")
# except ZeroDivisionError:
#     print(f"ERROR: {name} has no grades.")
# else:
#     print("== All student averages calculated ==")
# finally:
#     print("== End of calculation == ")

# grades = []
# # grades = [78, 99, 86, 100]
# print("welcome to averages program")
# try:
#     average = divide(sum(grades), len(grades))
#     print("The averager grade is", average)
# except ZeroDivisionError as e:
#     print(e)
#     print("There are no grades yet in your list. ")


runner()
