class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = m
        COLS = n
        memo = {}

        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1:
                return 0

            if r == ROWS-1 and c == COLS-1:
                return 1

            if (r,c) in memo:
                return memo[(r,c)]

            res = dfs(r+1, c) + dfs(r, c+1)
            memo[(r,c)] = res

            return res

        res = dfs(0, 0)
        return res
        