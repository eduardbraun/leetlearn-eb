# 1260.
# Shift 2D Grid
# https://leetcode.com/problems/shift-2d-grid/s
# approach would to think of it as a 1D array
# we can use m x n to calculate the one 1D array positions
def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    M, N = len(grid), len(grid[0])

    def posToVal(r, c):
        return r * N + c

    def valToPos(v):
        return [v // N, v % N]

    res = [[0] * N for i in range(M)]
    for r in range(M):
        for c in range(N):
            newVal = (posToVal(r, c) + k) % (M * N)
            newR, newC = valToPos(newVal)
            res[newR][newC] = grid[r][c]
    return res