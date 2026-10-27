"""Library catalog and borrowing operations."""

from datetime import date, timedelta

from src.errors import LibraryError

LOAN_DAYS = 14


class Library:
    """Manages the catalog, the members and the loans."""

    def __init__(self, clock=date.today):
        self.books = {}
        self.members = {}
        self.loans = {}
        self._clock = clock
        self.reservations = {}

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
        self.loans[(member_id, isbn)] = self._clock()

    def return_book(self, member_id, isbn):
        """Take a book back from a member."""
        member = self._require_member(member_id)
        book = self._require_book(isbn)
        member.return_book(isbn)
        fee = self.late_fee(member_id, isbn)
        del self.loans[(member_id, isbn)]
        book.return_copy()
        return fee

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
        return self._search("title", title)

    def search_by_author(self, author):
        """Return the books whose author contains the text."""
        return self._search("author", author)

    def get_available_books(self):
        """Return the books that have at least one free copy."""
        return [book for book in self.books.values() if book.is_available()]

    def _search(self, field, text):
        """Return the books whose field contains the text, ignoring case."""
        text = text.lower()
        return [book for book in self.books.values() if text in getattr(book, field).lower()]

    def due_date(self, member_id, isbn):
        """Return the date the loan has to be returned by."""
        return self.loans[(member_id, isbn)] + timedelta(days=LOAN_DAYS)

    def late_fee(self, member_id, isbn):
        """Return the fee owed for a borrowed book."""
        rate = self._require_member(member_id).category.late_fee_rate
        return self._days_overdue(member_id, isbn) * rate

    def total_late_fees(self, member_id):
        """Return the fees owed for all books a member holds."""
        member = self._require_member(member_id)
        return sum(self.late_fee(member_id, isbn) for isbn in member.borrowed_books)

    def _days_overdue(self, member_id, isbn):
        """Return how many days past the due date a loan is, never negative."""
        return max((self._clock() - self.due_date(member_id, isbn)).days, 0)

    def reserve_book(self, member_id, isbn):
        """Queue a member for a book that has no free copies."""
        self._require_member(member_id)
        if self._require_book(isbn).is_available():
            raise LibraryError("Book is available, borrow it instead")
        queue = self.reservations.setdefault(isbn, [])
        if member_id in queue:
            raise LibraryError("Member already reserved this book")
        queue.append(member_id)

    def reservation_queue(self, isbn):
        """Return the member ids waiting for a book, first in line first."""
        return list(self.reservations.get(isbn, []))
