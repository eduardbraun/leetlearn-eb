# 36.
# Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
def isValidSudoku(self, board: List[List[str]]) -> bool:
    cols = collections.defaultdict(set) # each row will have one set
    rows = collections.defaultdict(set) # each col will have on set
    squares = collections.defaultdict(set) # key = (r /3, c /3)

    # board is 9x9
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            # determine if the board is valid
            if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    # check if the value exist in the squares already
                    board[r][c] in squares[(r // 3, c // 3)]):
                    # invalid
                    return False
            # we add to the used which is used to determine if the board is valid
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    # is valid
    return True