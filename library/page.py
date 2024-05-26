"""Defines the Page class.

This class offers methods to extract text from the numerical
representation of a page.

"""

from .constants import *

class Page:
    def __init__(self, p):
        self.p = p

    @property
    def text(self):
        return self.get_text()

    def get_text(self):
        """Returns the text representation for this page."""
        p = self.p
        s = ""
        while p > 0:
            p, c = divmod(p, len(CHARSET))
            s += CHARSET[c]
        while len(s) < CHARS_PER_PAGE:
            s = " " + s
        s = s[::-1]
        lines = [
            s[i:i + CHARS_PER_LINE]
            for i in range(0, CHARS_PER_PAGE, CHARS_PER_LINE)
        ]
        return "\n".join(lines)
