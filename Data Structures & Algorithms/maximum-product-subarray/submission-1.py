class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        prefix = suffix = 0

        for i in range(n):
            if prefix != 0:
                prefix = prefix * nums[i]
            else:
                prefix = nums[i]

            if suffix != 0:
                suffix = suffix * nums[n - i - 1]
            else:
                suffix = nums[n - i - 1]

            res = max(res, prefix, suffix)

        return res

        