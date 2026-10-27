"""Tests for the Book class."""
# pylint: disable=missing-function-docstring

from src.book import Book


def test_book_can_be_created_with_isbn_title_and_author():
    book = Book("1234567890", "Test Book", "Author")
    assert (book.isbn, book.title, book.author) == ("1234567890", "Test Book", "Author")


def test_book_has_one_copy_by_default():
    assert Book("1234567890", "Test Book", "Author").available_copies == 1


def test_book_has_available_copies():
    book = Book("1234567890", "Test Book", "Author", copies=5)
    assert (book.total_copies, book.available_copies) == (5, 5)


def test_book_is_available_when_copies_exist():
    book = Book("1234567890", "Test Book", "Author", copies=1)
    assert book.is_available() is True
