"""Book model for the library."""


class Book:
    """A book in the catalog."""

    def __init__(self, isbn, title, author, copies=1):
        if len(isbn) not in (10, 13):
            raise ValueError("ISBN must have 10 or 13 digits")
        self.isbn = isbn
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available_copies = copies

    def is_available(self):
        """Return True when at least one copy can be borrowed."""
        return self.available_copies > 0
