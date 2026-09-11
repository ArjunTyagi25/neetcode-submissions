class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L = 0
        res = float('-inf')
        curr_sum = 0

        for R in range(len(nums)):
            curr_sum += nums[R]
            res = max(res, curr_sum)

            if curr_sum < 0:
                L = R+1
                curr_sum = 0

        return res