# --- Directions
# Given a string, return the character that is most
# commonly used in the string.
# --- Examples
# maxChar("abcccccccd") == "c"
# maxChar("apple 1231111") == "1"

from collections import Counter

def max_char(strg):
    return Counter(strg).most_common(1)[0][0]
