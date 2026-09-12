class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
        memo = {}

        def rec(r, c):
            if r == ROWS-1:
                return triangle[r][c]

            if (r,c) in memo:
                return memo[(r, c)]

            res = triangle[r][c] + min(rec(r+1, c), rec(r+1, c+1))
            memo[(r, c)] = res

            return res

        return rec(0, 0)
