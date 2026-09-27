class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def rec(i, buying_day):
            if i == len(prices):
                return 0

            if (i, buying_day) in memo:
                return memo[(i, buying_day)]

            profit_1, profit_2 = 0, 0
            # If I am holding a share, I can either sell today or continue holding
            if buying_day != -1:
                profit_1 = max(prices[i] - prices[buying_day] + rec(i+1, -1), rec(i+1, buying_day))

            # If I am not holding a share, I can either buy today or skip doing anything
            if buying_day == -1:
                profit_2 = max(rec(i+1, i), rec(i+1, -1))

            memo[(i, buying_day)] = max(profit_1, profit_2)
            return max(profit_1, profit_2)

        return rec(0, -1)