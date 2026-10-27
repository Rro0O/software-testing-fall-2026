"""Shared helpers for the tests."""

from src.book import Book
from src.library import Library
from src.member import Member

ISBN = "1234567890"


def make_library(copies=1):
    """Build a library with one book and one member."""
    library = Library()
    library.add_book(Book(ISBN, "Clean Code", "Robert Martin", copies=copies))
    library.register_member(Member("m1", "Ana"))
    return library
