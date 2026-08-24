class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, curr_comb, curr_total):
            if curr_total == target:
                res.append(curr_comb.copy())
                return

            for j in range(i, len(nums)):
                if curr_total + nums[j] > target:
                    return
                curr_comb.append(nums[j])
                backtrack(j, curr_comb, curr_total + nums[j])
                curr_comb.pop()

        backtrack(0, [], 0)

        return res

        