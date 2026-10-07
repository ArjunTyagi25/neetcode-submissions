class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
    
        def rec(i, runningTotal):
            if i == len(nums):
                if runningTotal == target:
                    return 1
                else:
                    return 0
            state = (i, runningTotal)
            if state in memo:
                return memo[state]

            res = rec(i+1, runningTotal + nums[i]) + rec(i+1, runningTotal - nums[i])
            memo[state] = res

            return res

        return rec(0, 0)