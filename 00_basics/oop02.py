class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight} gr."

    @classmethod
    # specify type inside the class
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)


# class Device:
#     def __init__(self, name, connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected = True

#     def __str__(self):
#         return f"Device {self.name} ({self.connected_by})."

#     def disconnect(self):
#         self.connected = False
#         print(f"Device {self.name} disconnected")


# class Printer(Device):
#     def __init__(self, name, connected_by, capacity):
#         super().__init__(name, connected_by)
#         self.capacity = capacity
#         self.pages_remaining = capacity

#     def __str__(self):
#         status = "Connected" if self.connected else "Disconnected"
#         return f"{super().__str__()} ({self.pages_remaining} remaing pages). Status: {status}"

#     def print(self, pages):
#         if not self.connected:
#             print(f"Your printer {self.name} is not connected.")
#         print(f"Printing {pages} pages.")
#         self.pages_remaining -= pages


# hp = Printer("HP", "USB", 500)
# print("===")
# print(hp)
# hp.print(20)
# print(hp)
# hp.disconnect()
# print(hp)
# hp.print(20)
