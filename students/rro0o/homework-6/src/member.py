"""Library member model."""


class Member:
    """A registered library member."""

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        self.max_borrow_limit = 3
