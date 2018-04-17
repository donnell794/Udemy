# --- Directions
# Write a function that accepts a positive number N.
# The function should console log a step shape
# with N levels using the # character.  Make sure the
# step has spaces on the right hand side!
# --- Examples
#   steps(2)
#       '# '
#       '##'
#   steps(3)
#       '#  '
#       '## '
#       '###'
#   steps(4)
#       '#   '
#       '##  '
#       '### '
#       '####'

def steps(n, row = 0, stair = ''):
    if n == row:
        return
    if n == len(stair):
        print(stair)
        return steps(n, row + 1)

    add = '#' if len(stair) <= row else ' '
    steps(n, row, stair + add)

# def steps(n):
#     for i in range(n):
#         stair = ''
#         for x in range(n):
#             if x <= i:
#                 stair += '#'
#             else: stair += ' '
#         print(stair)
