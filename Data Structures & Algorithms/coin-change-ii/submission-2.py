class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def rec(remaining_amount, curr_coin_index):
            if curr_coin_index == len(coins) or remaining_amount < 0:
                return 0

            if remaining_amount == 0:
                return 1

            if (remaining_amount, curr_coin_index) in memo:
                return memo[(remaining_amount, curr_coin_index)]

            res = rec(remaining_amount - coins[curr_coin_index], curr_coin_index) + rec(remaining_amount, curr_coin_index+1)
            memo[(remaining_amount, curr_coin_index)] = res
            return res
            
        return rec(amount, 0)
        