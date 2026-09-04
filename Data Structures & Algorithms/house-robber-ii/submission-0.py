class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.rec(0, nums[:-1], {}), self.rec(0, nums[1:], {})) 

    def rec(self, i, sub_nums, indexToValues):
        if i >= len(sub_nums):
            return 0

        if i in indexToValues:
            return indexToValues[i]

        indexToValues[i] = max(sub_nums[i] + self.rec(i+2, sub_nums, indexToValues), self.rec(i+1, sub_nums, indexToValues))
        return indexToValues[i]
