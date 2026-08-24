class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, curr_comb, curr_total):
            if curr_total == target:
                res.append(curr_comb.copy())
                return

            if i == len(nums) or curr_total > target:
                return

            curr_comb.append(nums[i])
            backtrack(i, curr_comb, curr_total + nums[i])
            curr_comb.pop()
            backtrack(i+1, curr_comb, curr_total)

        backtrack(0, [], 0)

        return res

        