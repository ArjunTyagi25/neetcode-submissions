class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0

            num_land = 1
            grid[r][c] = 0

            num_land += dfs(r+1, c)
            num_land += dfs(r-1, c)
            num_land += dfs(r, c+1)
            num_land += dfs(r, c-1)

            return num_land

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_lands = dfs(r, c)
                    res = max(res, num_lands)

        return res
        