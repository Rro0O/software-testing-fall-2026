"""Book model for the library."""


class Book:
    """A book in the catalog."""

    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
