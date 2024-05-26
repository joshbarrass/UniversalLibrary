"""Helper functions."""

import math

# from https://arxiv.org/abs/2204.04342
def fast_inverse(a, bits):
    m = 1 << bits
    bitmask = m - 1

    x = (3 * a) ^ 2
    y = 1 - a*x

    # must choose a k <= 5 s.t.:
    #   bits % k = 0
    #   bits % k is a power of 2
    k = 5
    while k > 0 and (
        bits % k != 0
        or int(math.log2(bits // k)) != math.log2(bits // k)
    ):
        k -= 1
    if k == 0:
        raise ValueError("no appropriate choice of k")

    p = int(math.log2(bits // k))
    for i in range(p):
        x = x * (1+y)
        x &= bitmask
        if i != p - 1:
            y *= y
            y &= bitmask
    return x
