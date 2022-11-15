# 118.
# Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
def generate(self, numRows: int) -> List[List[int]]:
    # generates 2d array with 1 initialized to be the size of the pascal triangle
    pascal = [[1] * (i + 1) for i in range(numRows)]
    for i in range(numRows):
        # we will start from the second row of the pascal triangle since the first two rows are just once
        # in the case we defined range to be from 1 to n where n has to be bigger than 1
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    return pascal