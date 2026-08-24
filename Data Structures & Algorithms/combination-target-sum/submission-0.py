class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr_combination, res = [], []
        self.helper(0, nums, curr_combination, res, target)
        return res

    def helper(self, i, nums, curr_combination, res, target):
        if sum(curr_combination) == target:
            res.append(curr_combination.copy())
            return

        if sum(curr_combination) > target:
            return

        if i == len(nums):
            return

        for j in range(i, len(nums)):
            curr_combination.append(nums[j])
            self.helper(j, nums, curr_combination, res, target)
            curr_combination.pop()

        