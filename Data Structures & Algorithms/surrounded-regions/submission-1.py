class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        def checkRegion(r, c):
            if r < 0 or c < 0 or r > R-1 or c > C-1 or board[r][c] == "X" or board[r][c] == "NS":
                return

            board[r][c] = "NS"

            checkRegion(r+1, c)
            checkRegion(r-1, c)
            checkRegion(r, c+1)
            checkRegion(r, c-1)

        for c in range(C):
            if board[0][c] == "O":
                checkRegion(0, c)
            if board[R-1][c] == "O":
                checkRegion(R-1, c)

        for r in range(R):
            if board[r][0] == "O":
                checkRegion(r, 0)
            if board[r][C-1] == "O":
                checkRegion(r, C-1)

        for r in range(R):
            for c in range(C):
                if board[r][c] == "NS":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"



        