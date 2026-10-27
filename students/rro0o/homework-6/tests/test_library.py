"""Tests for the Library class."""
# pylint: disable=missing-function-docstring

import pytest

from src.book import Book
from src.errors import LibraryError
from src.library import Library
from src.member import Member

from tests.helpers import ISBN, make_library


def test_added_book_can_be_found_by_isbn():
    library = Library()
    book = Book(ISBN, "Clean Code", "Robert Martin")
    library.add_book(book)
    assert library.find_book(ISBN) is book


def test_adding_same_isbn_twice_raises_error():
    library = Library()
    library.add_book(Book(ISBN, "Clean Code", "Robert Martin"))
    with pytest.raises(LibraryError):
        library.add_book(Book(ISBN, "Other", "Someone"))


def test_registered_member_can_be_found_by_id():
    library = Library()
    member = Member("m1", "Ana")
    library.register_member(member)
    assert library.find_member("m1") is member


def test_registering_same_member_twice_raises_error():
    library = Library()
    library.register_member(Member("m1", "Ana"))
    with pytest.raises(LibraryError):
        library.register_member(Member("m1", "Bo"))


def test_borrow_book_takes_a_copy_from_the_catalog():
    library = make_library()
    library.borrow_book("m1", ISBN)
    assert library.find_book(ISBN).available_copies == 0


def test_borrow_book_records_the_loan_on_the_member():
    library = make_library()
    library.borrow_book("m1", ISBN)
    assert library.find_member("m1").borrowed_books == [ISBN]
