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
        book = self._require_book(isbn)
        member = self._require_member(member_id)
        if not member.can_borrow():
            raise LibraryError("Member reached the borrow limit")
        book.borrow()
        member.add_borrowed_book(isbn)

    def return_book(self, member_id, isbn):
        """Take a book back from a member."""
        member = self._require_member(member_id)
        member.return_book(isbn)
        self._require_book(isbn).return_copy()

    def _require_book(self, isbn):
        """Return the book or raise if it is not in the catalog."""
        if isbn not in self.books:
            raise LibraryError("Unknown book")
        return self.books[isbn]

    def _require_member(self, member_id):
        """Return the member or raise if not registered."""
        if member_id not in self.members:
            raise LibraryError("Unknown member")
        return self.members[member_id]

    def search_by_title(self, title):
        """Return the books whose title contains the text."""
        text = title.lower()
        return [book for book in self.books.values() if text in book.title.lower()]

    def search_by_author(self, author):
        """Return the books whose author contains the text."""
        text = author.lower()
        return [book for book in self.books.values() if text in book.author.lower()]
