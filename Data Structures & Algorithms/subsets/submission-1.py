class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, curr_subset):
            if i == len(nums):
                res.append(curr_subset.copy())
                return 

            curr_subset.append(nums[i])
            backtrack(i+1, curr_subset)
            curr_subset.pop()

            backtrack(i+1, curr_subset)

        backtrack(0, [])

        return res
        