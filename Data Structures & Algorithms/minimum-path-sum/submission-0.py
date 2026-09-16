class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        memo = {}

        def rec(r,c):
            if r == ROWS-1 and c == COLS-1:
                return grid[r][c]

            if r > ROWS-1 or c > COLS-1:
                return float('inf')

            if (r,c) in memo:
                return memo[(r,c)]

            res = grid[r][c] + min(rec(r+1,c), rec(r, c+1))
            memo[(r,c)] = res
            return res
        
        return rec(0,0)