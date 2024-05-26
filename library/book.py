"""Defines the Book class.

This class offers methods to extract pages from the numerical
representation of a book.

"""

from .constants import *
from .page import Page

PAGE_BITMASK = 2**BITS_PER_PAGE - 1

class Book:
    def __init__(self, b):
        self.b = b

    def get_page(self, n):
        """Get the nth page from the book."""
        if n >= PAGES_PER_BOOK:
            raise ValueError(
                f"n must be between 0 and {PAGES_PER_BOOK-1}"
            )

        return Page((self.b >> n) & PAGE_BITMASK)
