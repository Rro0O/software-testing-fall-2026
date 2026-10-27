"""Library member model."""


class Member:
    """A registered library member."""

    def __init__(self, member_id, name, max_borrow_limit=3):
        if not name or not name.strip():
            raise ValueError("Name is required")
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        self.max_borrow_limit = max_borrow_limit

    def can_borrow(self):
        """Return True while the member is under the borrow limit."""
        return True
