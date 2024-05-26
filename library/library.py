"""Defines the Library class.

This contains everything that is needed to move between books in the
library.

"""

import random
from .constants import *
from .helpers import fast_inverse
from .book import Book

class Library:
    def __init__(self, b0: int, c: int):
        self.b0 = b0
        self.c = c
        if not c & 1:
            raise ValueError("c must be odd")

        self.c_inv = fast_inverse(c, BITS_PER_BOOK)

    def get_book(self, n: int):
        """Get the nth book from the library.

        This returns the raw number corresponding to book n, *not* the
        text or individual pages.
        """
        return Book((self.b0 + n * self.c) & MOD_BITMASK)

    def get_n_for_book(self, b: Book):
        """Determine which n will produce the desired book.

        The book should be inputted as the raw number corresponding to
        the book, *not* the text.
        """
        n = (b.b - self.b0) * self.c_inv
        return n & MOD_BITMASK

class DefaultLibrary(Library):
    def __init__(self):
        rng = random.Random()
        rng.seed(123456)
        b0 = random.randint(PHI, MODULUS - 1)
        c = random.randint(PHI, MODULUS - 1) | 1

        super().__init__(b0, c)
