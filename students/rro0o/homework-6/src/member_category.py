"""Membership categories with their borrowing rules."""

from enum import Enum


class MemberCategory(Enum):
    """Member types, valued by how many books they may borrow."""

    STUDENT = 3
    FACULTY = 5
    PUBLIC = 2

    @property
    def borrow_limit(self):
        """Return how many books this category may hold at once."""
        return self.value
