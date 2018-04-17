# --- Directions
# Given an integer, return an integer that is the reverse
# ordering of numbers.
# --- Examples
#   reverseInt(15) == 51
#   reverseInt(981) == 189
#   reverseInt(500) == 5
#   reverseInt(-15) == -51
#   reverseInt(-90) == -9

from math import copysign

def reverse_int(n):
    rev_n = str(n)[::-1] if n >= 0 else str(n)[:0:-1]
    return copysign(int(rev_n), n)
