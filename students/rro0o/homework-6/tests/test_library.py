"""Tests for the Library class."""
# pylint: disable=missing-function-docstring

from src.book import Book
from src.library import Library
from src.member import Member

ISBN = "1234567890"


def test_added_book_can_be_found_by_isbn():
    library = Library()
    book = Book(ISBN, "Clean Code", "Robert Martin")
    library.add_book(book)
    assert library.find_book(ISBN) is book
