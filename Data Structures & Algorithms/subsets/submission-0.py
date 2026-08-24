class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        current_subset, result = [], []
        self.helper(0, nums, current_subset, result)

        return result

    def helper(self, i, nums, current_subset, result):
        if i >= len(nums):
            result.append(current_subset.copy())
            return

        current_subset.append(nums[i])
        self.helper(i+1, nums, current_subset, result)

        current_subset.pop()
        self.helper(i+1, nums, current_subset, result)

        return
        