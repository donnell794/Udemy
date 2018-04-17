# --- Directions
# Write a function that accepts a positive number N.
# The function should console log a pyramid shape
# with N levels using the # character.  Make sure the
# pyramid has spaces on both the left *and* right hand sides
# --- Examples
#   pyramid(1)
#       '#'
#   pyramid(2)
#       ' # '
#       '###'
#   pyramid(3)
#       '  #  '
#       ' ### '
#       '#####'

def pyramid(n, row = 0, level = ''):
    if row == n:
        return
    max_width = n * 2 - 1
    if len(level) == max_width:
        print(level)
        return pyramid(n, row + 1)
    midpoint = max_width // 2
    if (midpoint - row) <= len(level) <= (midpoint + row):
        level += '#'
    else: level += ' '
    pyramid(n, row, level)
