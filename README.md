# The Universal Library

The Universal Library is designed to contain every possible book of a given character set. It is inspired by Jorge Luis Borges' short story _The Library of Babel_, and [the website of the same name](libraryofbabel.info). By containing every possible book, the library can contain every text that has been, or will ever be, written, as well as every slight variation and every book of gibberish. This program offers a way to retrieve any book from the enormous library, or to search the library for a book containing a certain text.

The character set used in this software extends that of the original Library of Babel, which uses 25 characters, and that of [libraryofbabel.info](libraryofbabel.info), which uses 29 characters. Here. a set of 64 characters is used, and each book contains 2²⁰ characters. At 6 bits per character, each book represents 768KiB, and the library contains 2⁵²⁴²⁸⁸⁰ unique books; around 1.4×10¹⁵⁷⁸²⁶⁴ books.

## Theory

This section aims to simplify and explain how this software works mathematically, in the hopes of providing some insight to others.

Each book in the library contains 512 pages, with each page containing 32 lines, and each line containing 64 characters. We have 64 possible characters, so each character can be represented by 6 bits. In total, each book can be represented by $512\times 32\times 64\times 6 = 6291456$ bits. Instead of thinking about this as some 1048576 charcaters, we can instead think of a single book as being one 6291456-bit number, so every single book in the library can be represented by a number between $0$ and $2^6291456 - 1$. For any larger numbers, we can just discard all but the last 6291456 bits; for example, if we picked $2^6291456$, from right to left we would have 6291456 zeroes, followed by a single one. Discarding everything after those 6291456 zeroes leaves us with 0, and so book $2^6291456$ is the same as book $0$. Mathematically, we can express this using modular arithmetic; for any number, $a$, we can obtain the corresponding book, $b$, by dividing by $2^6291456$ and keeping the remainder! Written mathematically, 

```math
b = a\ \left(\mod\ 2^6291456\right)\ .
```

The library is not truly random. In fact, using randomness would make it more difficult to guarantee that every possible book exists in the library. Instead, the aim is to create something that _looks random enough_, i.e. if you start at book 0 and read in sequence, everything will look like gibberish, but where we can easily figure out where a book of interest lies within the library. The way this is achieved is by picking two random values: the starting book, $b_0$, and a constant, $c$. The nth book is obtained as

```math
b_n = b_0 + nc\ \left(\mod\ 2^6291456\right)\ .
```

This way, if $b_0 + nc > 2^6291456 - 1$, the value loops back around to be inside the necessary range. To ensure every possible book is reachable via this formula, $c$ must be chosen such that the only number dividing both $c$ and $2^6291456$ is 1. This is an easy condition to satisfy, requiring only that $c$ is odd! If both numbers are large and random, each subsequent book will bear little resemblance to the previous, and will, for all intents and purposes, appear to be another random book. However, this equation can be rearranged to find which $n$ will give us a book of our choosing, $b_n$:

```math
n = \left( b_n - b_0 \right)c^{-1} \ \left(\mod\ 2^6291456\right)\ ,
```

where $c^{-1}$ is the integer that satisfies the equation $cc^{-1} = 1 \ \left(\mod\ 2^6291456\right)$. The equation for $c^{-1}$ is known from Euler's theorem; it can be written as

```math
c^{-1} = c^{\phi\left( 2^6291456 \right)-1} = c^{2^6291455 - 1} \ \left(\mod\ 2^6291456\right)\ ,
```

but computing this directly is very slow (similar computations are used to create time-locked puzzles [1]!). Instead, we can take advantage of the algorithm developed by Hurchalla [2], taking advantage of the fact that our base is a power of 2 to compute this in only a few multiplications. Now it is possible to quickly find _any_ $b_n$ in the library!

## References

[1] R. L. Rivest, A. Shamir, D. A. Wagner, _Time-lock puzzles and timed-release crypto_, [dspace.mit.edu](https://dspace.mit.edu/bitstream/handle/1721.1/149822/MIT-LCS-TR-684.pdf)
[2] J. Hurchalla, _An improved integer modular multiplicative inverse (modulo 2^w)_, [arxiv.org](https://arxiv.org/abs/2204.04342)
