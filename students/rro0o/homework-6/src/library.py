"""Library catalog and borrowing operations."""

from src.errors import LibraryError


class Library:
    """Manages the catalog, the members and the loans."""

    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        """Add a book to the catalog."""
        if book.isbn in self.books:
            raise LibraryError("Book already in the catalog")
        self.books[book.isbn] = book

    def find_book(self, isbn):
        """Return the book with this ISBN."""
        return self.books[isbn]

    def register_member(self, member):
        """Register a new member."""
        self.members[member.member_id] = member

    def find_member(self, member_id):
        """Return the member with this id."""
        return self.members[member_id]
