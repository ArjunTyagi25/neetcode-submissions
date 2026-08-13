class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(9):
            row_values = set()
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] in row_values:
                        return False
                    else:
                        row_values.add(board[r][c])

        for c in range(9):
            col_values = set()
            for r in range(9):
                if board[r][c] != ".":
                    if board[r][c] in col_values:
                        return False
                    else:
                        col_values.add(board[r][c])

        for r_start in [0, 3, 6]:
            for c_start in [0, 3, 6]:
                grid_values = set()
                for r in range(r_start, r_start+3):
                    for c in range(c_start, c_start+3):
                        if board[r][c] != ".":
                            if board[r][c] in grid_values:
                                return False
                            else:
                                grid_values.add(board[r][c])

        return True
        