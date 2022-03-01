#!/usr/bin/env python3

# Generate Windows-like activation key
# for example 'W8H74-7F63C-Y44W4-379XJ-23FMF'

from random import choices, choice, shuffle
from string import ascii_uppercase, digits


def gen_random_key_block(l=2, d=3):
    """Generate random key block, number of letters = l, number of digits = d
    """
    rnd_lst = choices(ascii_uppercase, k=l) + choices(digits[1:], k=d)
    shuffle(rnd_lst)
    return ''.join(rnd_lst)


def gen_random_key(l=2, d=3, n=5):
    """Generate random key, number of letters = l, number of digits = d,
    number of blocks = n
    """
    lst = []
    for block in range(n):
        lst.append(gen_random_key_block(l, d))
    return '-'.join(lst)


if __name__ == '__main__':
    print(gen_random_key())
