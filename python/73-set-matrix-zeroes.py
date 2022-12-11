# 73.
# Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # O(1) solution
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False
    # determine which rows/cols need to be zeroed

    for i in range(ROWS):
        for j in range(COLS):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                if i > 0:
                    matrix[i][0] = 0
                else:
                    rowZero = True

    # zero out starting from 1 - n
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    # check if we need to zero out the starting values row,col
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0