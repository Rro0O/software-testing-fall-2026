"""Library member model."""

from src.errors import LibraryError


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
        return len(self.borrowed_books) < self.max_borrow_limit

    def add_borrowed_book(self, isbn):
        """Record that the member borrowed the book with this ISBN."""
        if not self.can_borrow():
            raise LibraryError("Borrow limit reached")
        if isbn in self.borrowed_books:
            raise LibraryError("Book already borrowed")
        self.borrowed_books.append(isbn)
