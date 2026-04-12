"""
Library Management System
Objective:

Create a library management system with books, members, and a library class. Use inheritance, encapsulation, and getters/setters.
Requirements:

Book Class:

Attributes: title, author, isbn, is_available (private)
Methods: __init__, get_title, get_author, get_isbn, is_available, set_available

Member Class:

Attributes: name, member_id, borrowed_books (private list)
Methods: __init__, get_name, get_member_id, borrow_book, return_book

Library Class:

Attributes: books (private list), members (private list)
Methods: __init__, add_book, remove_book, register_member, lend_book, return_book
"""

from abc import ABC, abstractmethod
from types import prepare_class

Book_list = []
Register_member_list = []


class Book(ABC):
    def __init__(self, book_title: str, author: str, isbn):
        self.__book_title = book_title
        self.__author = author
        self.__isbn = isbn

    @property
    def get_title(self):
        return self.__book_title

    @property
    def get_author(self):
        return self.__author

    @property
    def get_isbn(self):
        return self.__isbn

    def Dispay_book_info(self):
        print(
            f"{self.get_title} created by {self.get_author}'s Book isbm number is {self.get_isbn}"
        )


class Member(Book):
    def __init__(
        self,
        # Member class Attribute
        member_name: str,
        member_id,
        borrowed_books: str,
    ):
        self.__meber_name = member_name
        self.__meber_id = member_id
        self.__borrowed_books = borrowed_books

    @property
    def get_member_name(self):
        return self.__meber_name

    @property
    def get_member_id(self):
        return self.__meber_id

    @property
    def borrow_book(self):
        return self.__borrowed_books

    @borrow_book.setter
    def borrow_book(self, borrow):

        if borrow in Book_list:
            print(f"Heres your book {borrow}")
            Book_list.remove(borrow)
            self.__borrowed_books = borrow
        else:
            print(f"Sorry book {borrow} is not available")

    def Dispay_member_info(self):
        print(
            f"{self.get_member_name}'s ID is {self.get_member_id} the book he borrowed is {self.borrow_book}"
        )


class Library(Member, Book):
    def __init__(
        self,
        # Library class Attribute
        add_book: str,
        remove_book: str,
        register_member_name: str,
    ):
        self.add_book = add_book
        self.remove_book = remove_book
        self.register_member_name = register_member_name

    @property
    def add_book_(self):
        return self.add_book

    @add_book_.setter
    def add_book_(self, add_book):
        if add_book == str:
            Book_list.append(add_book)
            self.add_book = add_book
        else:
            raise ValueError("Book is invalid")

    @property
    def remove_book_(self):
        return self.remove_book

    @remove_book_.setter
    def remove_book_(self, remove_book):
        if remove_book == str:
            Book_list.remove(remove_book)
            self.remove_book = remove_book
        else:
            raise ValueError("Book is invalid")

    @property
    def register(self):
        return self.register_member_name

    @register.setter
    def register(self, register_member):
        if register_member not in Register_member_list:
            Register_member_list.append(register_member)
            print(Register_member_list)
        else:
            print("Member already in list")

    def Dispay_Library_info(self):
        print(
            f"{self.add_book} added and {self.remove_book} removed with {self.register} as member"
        )
        print(Register_member_list)
        print(Book_list)


B1 = Book("Python", "Ved", "CESA89745")
B1.Dispay_book_info()
M1 = Member("Tux", 874562, "Python")
M1.Dispay_member_info()
# M1.borrow_book = "python22"
# M1.Dispay_member_info()
# L1 = Library("java", "python", "kay")
# L1.Dispay_Library_info()
