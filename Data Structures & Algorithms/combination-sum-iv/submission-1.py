class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def rec(curr_sum):
            if curr_sum > target:
                return 0

            if curr_sum == target:
                return 1

            if curr_sum in memo:
                return memo[curr_sum]

            res = 0
            for num in nums:
                res += rec(curr_sum + num)

            memo[curr_sum] = res
            return res

        return rec(0)