# 733.
# Flood Fill
# https://leetcode.com/problems/flood-fill/
def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    maxRows = len(image)
    maxColumns = len(image[0])

    def dfs(row, col, targetValue):
        if row >= maxRows or row < 0 or col >= maxColumns or col < 0 or image[row][col] == newColor:
            return

        if image[row][col] != targetValue:
            return

        image[row][col] = newColor

        dfs(row - 1, col, targetValue)
        dfs(row + 1, col, targetValue)
        dfs(row, col - 1, targetValue)
        dfs(row, col + 1, targetValue)

    source = image[sr][sc]

    dfs(sr, sc, source)

    return image