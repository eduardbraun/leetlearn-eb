# 54.
# Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    res = []
    left = 0
    right = len(matrix[0])
    top = 0
    bottom = len(matrix)

    while left < right and top < bottom:
        # get every i in the top row going left to right
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # get every i in the right col going top to bottom
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        # check left < right as well as top < bottom other wise we are done already
        if not (left < right and top < bottom):
            break

        # get every i in the bottom row going right to left
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        # get every i in the left col going bottom to top
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
    return res
