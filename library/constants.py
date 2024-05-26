"""Contains all constants for the program."""

import string
import math

CHARSET = " " + string.ascii_lowercase + string.digits + '!"#%&\'()*+,-./:;<=>?@[\\]^_|'

# ensure this is an integer!
BITS_PER_CHAR = math.log2(len(CHARSET))
assert BITS_PER_CHAR == int(BITS_PER_CHAR)
BITS_PER_CHAR = int(BITS_PER_CHAR)

CHARS_PER_LINE = 64
LINES_PER_PAGE = 32
CHARS_PER_PAGE = CHARS_PER_LINE * LINES_PER_PAGE
BITS_PER_PAGE = CHARS_PER_PAGE * BITS_PER_CHAR
PAGES_PER_BOOK = 512
CHARS_PER_BOOK = CHARS_PER_PAGE * PAGES_PER_BOOK
BITS_PER_BOOK = BITS_PER_CHAR * CHARS_PER_BOOK

MODULUS = 1 << BITS_PER_BOOK
MOD_BITMASK = MODULUS - 1
PHI = 1 << (BITS_PER_BOOK - 1)
