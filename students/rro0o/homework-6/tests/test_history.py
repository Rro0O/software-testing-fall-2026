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
