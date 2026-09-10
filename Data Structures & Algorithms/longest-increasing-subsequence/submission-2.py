class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def rec(curr_index, prev_index):
            if curr_index == len(nums):
                return 0

            if (curr_index, prev_index) in memo:
                return memo[(curr_index, prev_index)]
                
            res = 0
            if prev_index == -1 or nums[prev_index] < nums[curr_index]:
                res = max(res, 1 + rec(curr_index+1, curr_index))

            res = max(res, rec(curr_index+1, prev_index))
            memo[(curr_index, prev_index)] = res

            return res

        return rec(0, -1)