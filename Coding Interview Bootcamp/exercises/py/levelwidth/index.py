# --- Directions
# Given the root node of a tree, return
# an array where each element is the width
# of the tree at each level.
# --- Example
# Given:
#     0
#   / |  \
# 1   2   3
# |       |
# 4       5
# Answer: [1, 3, 2]

def level_width(root):
    arr = [root, 's']
    width = [0]
    while len(arr) > 1:
        node = arr.pop(0)
        if node == 's':
            arr.append('s')
            width.append(0)
        else:
            arr.extend(node.children[:])
            width[len(width) - 1] += 1
    return width
