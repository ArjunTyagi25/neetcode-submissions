class Solution:
    def numSquares(self, n: int) -> int:

        memo = {}
        def rec(remaining):
            if remaining < 0:
                return float('inf')

            if remaining == 0:
                return 0

            if remaining in memo:
                return memo[remaining]

            closest_square = int(math.sqrt(remaining))
            
            res = float('inf')
            for i in range(closest_square+1, 0, -1):
                res = min(res, 1 + rec(remaining - i*i))

            memo[remaining] = res

            return memo[remaining]

        return rec(n)
        