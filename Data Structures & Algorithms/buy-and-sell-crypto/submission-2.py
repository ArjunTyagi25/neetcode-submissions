class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buying_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] <= buying_price:
                buying_price = prices[i]
            else:
                profit = max(profit, prices[i] - buying_price)

        return profit
        