# --- Directions
# Given a string, return a new string with the reversed
# order of characters
# --- Examples
#   reverse('apple') == 'leppa'
#   reverse('hello') == 'olleh'
#   reverse('Greetings!') == '!sgniteerG'

def reverse(str):
    return str[::-1]

    # r_str = ""
    # for chr in str:
    #     r_str = chr + r_str
    # return r_str
