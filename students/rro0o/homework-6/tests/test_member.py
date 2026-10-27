"""Tests for the Member class."""
# pylint: disable=missing-function-docstring

import pytest

from src.errors import LibraryError
from src.member import Member


def test_member_starts_with_id_name_no_books_and_default_limit():
    member = Member("m1", "Ana")
    assert (member.member_id, member.name, member.borrowed_books, member.max_borrow_limit) == ("m1", "Ana", [], 3)


def test_member_accepts_custom_borrow_limit():
    assert Member("m1", "Ana", max_borrow_limit=5).max_borrow_limit == 5


@pytest.mark.parametrize("name", ["", "  "])
def test_blank_name_is_rejected(name):
    with pytest.raises(ValueError):
        Member("m1", name)


def test_new_member_can_borrow():
    assert Member("m1", "Ana").can_borrow() is True


def test_add_borrowed_book_records_isbn():
    member = Member("m1", "Ana")
    member.add_borrowed_book("1234567890")
    assert member.borrowed_books == ["1234567890"]


def test_member_at_limit_cannot_borrow():
    member = Member("m1", "Ana", max_borrow_limit=1)
    member.add_borrowed_book("1234567890")
    assert member.can_borrow() is False


def test_add_borrowed_book_beyond_limit_raises_error():
    member = Member("m1", "Ana", max_borrow_limit=1)
    member.add_borrowed_book("1234567890")
    with pytest.raises(LibraryError):
        member.add_borrowed_book("0987654321")


def test_borrowing_same_book_twice_raises_error():
    member = Member("m1", "Ana")
    member.add_borrowed_book("1234567890")
    with pytest.raises(LibraryError):
        member.add_borrowed_book("1234567890")


def test_return_book_removes_isbn():
    member = Member("m1", "Ana")
    member.add_borrowed_book("1234567890")
    member.return_book("1234567890")
    assert member.borrowed_books == []


def test_returning_unborrowed_book_raises_error():
    member = Member("m1", "Ana")
    with pytest.raises(LibraryError):
        member.return_book("1234567890")
