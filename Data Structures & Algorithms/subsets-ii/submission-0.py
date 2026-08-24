class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def backtrack(i, curr_subset):
            if i == len(nums):
                res.append(curr_subset.copy())
                return

            curr_subset.append(nums[i])
            backtrack(i+1, curr_subset)
            curr_subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, curr_subset)

        backtrack(0, [])

        return res
        