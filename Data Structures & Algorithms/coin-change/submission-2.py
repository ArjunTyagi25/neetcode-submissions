class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def rec(remaining_total):
            if remaining_total == 0:
                return 0

            if remaining_total < 0:
                return float('inf')

            if remaining_total in memo:
                return memo[remaining_total]

            res = float('inf')
            for coin in coins:
                res = min(res, 1 + rec(remaining_total - coin))

            memo[remaining_total] = res
            return res

        res = rec(amount)
        if res == float('inf'):
            return -1
        else:
            return res