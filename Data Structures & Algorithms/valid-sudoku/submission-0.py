class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grids = [[] for i in range(9)]
        cols = [[] for i in range(9)]

        # Check each row for duplicates
        for r in range(9):
            row_values = set()
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] not in row_values:
                        row_values.add(board[r][c])
                    else:
                        return False

        # Check each column for duplicates
        for c in range(9):
            col_values = set()
            for r in range(9):
                if board[r][c] != ".":
                    if board[r][c] not in col_values:
                        col_values.add(board[r][c])
                    else:
                        return False

        # Check each 3x3 grid
        for R in range(0, 9, 3):
            for C in range(0, 9, 3):
                grid_values = set()
                for r in range(R, R+3, 1):
                    for c in range(C, C+3, 1):
                        if board[r][c] != ".":
                            if board[r][c] not in grid_values:
                                grid_values.add(board[r][c])
                            else:
                                return False

        return True

