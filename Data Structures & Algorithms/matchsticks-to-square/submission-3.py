class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)

        if total_length % 4 != 0:
            return False

        target_side_len = total_length/4
        memo = {}

        def rec(i, side_1, side_2, side_3, side_4):
            if side_1 == side_2 == side_3 == side_4 == target_side_len:
                return True

            if i == len(matchsticks) or side_1 > target_side_len or side_2 > target_side_len or side_3 > target_side_len or side_4 > target_side_len:
                return False

            if (i, side_1, side_2, side_3, side_4) in memo:
                return memo[(i, side_1, side_2, side_3, side_4)]

            res = rec(i+1, side_1 + matchsticks[i], side_2, side_3, side_4) or rec(i+1, side_1, side_2 + matchsticks[i], side_3, side_4) or rec(i+1, side_1, side_2, side_3 + matchsticks[i], side_4) or rec(i+1, side_1, side_2, side_3, side_4 + matchsticks[i])

            memo[(i, side_1, side_2, side_3, side_4)] = res
            return res

        return rec(0, 0, 0, 0, 0)
        
