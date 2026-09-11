class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False

        target = target/2
        memo = {}

        def rec(i, remaining):
            if remaining == 0:
                return True
            
            if remaining < 0 or i == len(nums):
                return False

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            # Take the number
            res = rec(i+1, remaining - nums[i])
            res = res | rec(i+1, remaining)
            memo[(i, remaining)] = res
            return res

        return rec(0, target)

        