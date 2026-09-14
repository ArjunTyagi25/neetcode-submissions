class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def rec(holding, cooldown, i):
            if i == len(prices):
                return 0

            if (holding, cooldown, i) in memo:
                return memo[(holding, cooldown, i)]

            # If holding a share, I can either sell it at the current day or keep it
            if holding:
                sell = prices[i] + rec(False, True, i+1)
                keep = rec(True, False, i+1)
                memo[(holding, cooldown, i)] = max(sell, keep)
                return memo[(holding, cooldown, i)]
            # If I am in cooldown, I can just keep the share
            elif cooldown:
                memo[(holding, cooldown, i)] = rec(False, False, i+1)
                return memo[(holding, cooldown, i)]
            # Since both holding and cooldown were False, that means I can either buy at the current day or skip it
            else:
                buy = rec(True, False, i+1) - prices[i]
                skip = rec(False, False, i+1)
                memo[(holding, cooldown, i)] = max(buy, skip)
                return memo[(holding, cooldown, i)]

        return rec(False, False, 0)
