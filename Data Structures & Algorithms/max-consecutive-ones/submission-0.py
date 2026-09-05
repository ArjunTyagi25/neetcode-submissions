class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr_length = 0

        for i in nums:
            if i == 1:
                curr_length += 1
            else:
                res = max(res, curr_length)
                curr_length = 0

        res = max(res, curr_length)
        return res
        