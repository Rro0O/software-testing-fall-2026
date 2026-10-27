"""Tests for the Member class."""
# pylint: disable=missing-function-docstring

import pytest

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
