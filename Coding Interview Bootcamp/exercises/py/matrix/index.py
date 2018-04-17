# --- Directions
# Write a function that accepts an integer N
# and returns a NxN spiral matrix.
# --- Examples
#   matrix(2)
#     [[1, 2],
#     [4, 3]]
#   matrix(3)
#     [[1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]]
#  matrix(4)
#     [[1,   2,  3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10,  9,  8, 7]]

def matrix(n):
    #a = [x[:] for x in [[] * n] * n]
    a = [[0] * n for i in range(n)]
    print(a)
    count = 1
    startRow = startCol = 0
    endRow = endCol = n - 1
    while count <= n**2:
        #top
        for i in range(startCol, endCol + 1):
            a[startRow][i] = count
            count += 1
        startRow += 1

        #right
        for i in range(startRow, endRow + 1):
            a[i][endCol] = count
            count += 1
        endCol -= 1

        #bottom
        for i in range(endCol , startCol - 1, -1):
            a[endRow][i] = count
            count += 1
        endRow -= 1

        #left
        for i in range(endRow, startRow - 1, -1):
            a[i][startCol] = count
            count += 1
        startCol += 1

    return a
