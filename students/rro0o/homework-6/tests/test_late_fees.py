"""Tests for late fee calculation."""
# pylint: disable=missing-function-docstring

from datetime import date

import pytest

from src.book import Book
from src.member_category import MemberCategory
from tests.helpers import ISBN, FakeClock, make_library


def test_due_date_is_fourteen_days_after_borrowing():
    library = make_library(clock=FakeClock(date(2026, 1, 1)))
    library.borrow_book("m1", ISBN)
    assert library.due_date("m1", ISBN) == date(2026, 1, 15)


def test_no_late_fee_on_the_due_date():
    clock = FakeClock()
    library = make_library(clock=clock)
    library.borrow_book("m1", ISBN)
    clock.advance(14)
    assert library.late_fee("m1", ISBN) == 0
