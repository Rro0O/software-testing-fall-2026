"""Tests for the borrowing history."""
# pylint: disable=missing-function-docstring

from datetime import date

from src.book import Book
from src.library import HistoryRecord
from tests.helpers import ISBN, FakeClock, make_library


def test_borrow_is_recorded_in_the_member_history():
    library = make_library(clock=FakeClock(date(2026, 1, 1)))
    library.borrow_book("m1", ISBN)
    assert library.member_history("m1") == [HistoryRecord("m1", ISBN, "borrow", date(2026, 1, 1))]


def test_return_is_recorded_after_the_borrow():
    clock = FakeClock()
    library = make_library(clock=clock)
    library.borrow_book("m1", ISBN)
    clock.advance(2)
    library.return_book("m1", ISBN)
    assert [record.action for record in library.member_history("m1")] == ["borrow", "return"]


def test_most_borrowed_book_is_none_without_history():
    assert make_library().most_borrowed_book() is None


def test_most_borrowed_book_is_the_one_with_most_borrows():
    library = make_library()
    library.add_book(Book("0987654321", "Refactoring", "Fowler"))
    library.borrow_book("m1", "0987654321")
    library.return_book("m1", "0987654321")
    library.borrow_book("m1", ISBN)
    library.return_book("m1", ISBN)
    library.borrow_book("m1", ISBN)
    assert library.most_borrowed_book() == ISBN
