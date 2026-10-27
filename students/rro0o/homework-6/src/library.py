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
        if member.member_id in self.members:
            raise LibraryError("Member already registered")
        self.members[member.member_id] = member

    def find_member(self, member_id):
        """Return the member with this id."""
        return self.members[member_id]

    def borrow_book(self, member_id, isbn):
        """Lend a book to a member."""
        if isbn not in self.books:
            raise LibraryError("Unknown book")
        if member_id not in self.members:
            raise LibraryError("Unknown member")
        book = self.books[isbn]
        member = self.members[member_id]
        book.borrow()
        member.add_borrowed_book(isbn)
