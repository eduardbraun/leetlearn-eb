# 59.
# Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii/
def generateMatrix(self, n: int) -> List[List[int]]:
    ROWS = n
    COLS = n

    res = [[0 for i in range(COLS)] for i in range(ROWS)]

    top = 0
    right = ROWS
    left = 0
    bottom = COLS

    curNum = 1

    while left <= right and top <= bottom:
        # left to right
        for i in range(left, right):
            res[top][i] = curNum
            curNum += 1
        top += 1
        # top to bottom
        for i in range(top, bottom):
            res[i][right - 1] = curNum
            curNum += 1
        right -= 1
        # bottom to left
        for i in range(right - 1, left - 1, -1):
            res[bottom - 1][i] = curNum
            curNum += 1
        bottom -= 1
        # left to top
        for i in range(bottom - 1, top - 1, -1):
            res[i][left] = curNum
            curNum += 1
        left += 1

    return res