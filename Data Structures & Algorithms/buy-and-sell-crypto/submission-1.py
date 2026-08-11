class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        L, R = 0, 1
        max_profit = max(0, prices[R] - prices[L])

        while L != len(prices)-1:
            cur_profit = prices[R] - prices[L]
            max_profit = max(max_profit, cur_profit)

            if R == len(prices)-1:
                L += 1
            else:
                if cur_profit < 0:
                    L = R
                    R += 1
                else:
                    if R != len(prices)-1:
                        R += 1

        return max_profit
        