"""Library catalog and borrowing operations."""


class Library:
    """Manages the catalog, the members and the loans."""

    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        """Add a book to the catalog."""
        self.books[book.isbn] = book

    def find_book(self, isbn):
        """Return the book with this ISBN."""
        return self.books[isbn]
