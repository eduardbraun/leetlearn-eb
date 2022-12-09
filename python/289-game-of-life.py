# 289.
# Game of Life
# https://leetcode.com/problems/game-of-life/
def gameOfLife(self, board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    ROWS, COLS = len(board), len(board[0])

    def countNeighboars(r, c):
        nei = 0
        # starting at top left corner
        for i in range(r - 1, r + 2):
            # to the bottom right neighbor
            for j in range(c - 1, c + 2):
                # we skip if the possition is out of bound or if it is the same as r and c
                if ((i == r and j == c) or i < 0 or j < 0 or i == ROWS or j == COLS):
                    continue
                # we check if it is a 1 or 3, a 3 would mean that the cell has already been changed and is living on
                if board[i][j] in [1, 3]:
                    nei += 1
        return nei

    for r in range(ROWS):
        for c in range(COLS):
            nei = countNeighboars(r,c)

            if board[r][c] == 1:
                if nei in [2, 3]:
                    board[r][c] = 3
            elif nei == 3:
                    board[r][c] = 2
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 1:
                board[r][c] = 0
            elif board[r][c] in [2, 3]:
                board[r][c] = 1