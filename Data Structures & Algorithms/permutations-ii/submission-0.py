class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(curr_perm, available_nums):
            if len(curr_perm) == len(nums):
                res.append(curr_perm.copy())
                return

            for i in range(len(available_nums)):
                if i > 0 and available_nums[i] == available_nums[i-1]:
                    continue

                available_nums_copy = available_nums.copy()
                curr_perm.append(available_nums[i])
                available_nums_copy.pop(i)
                
                backtrack(curr_perm, available_nums_copy)

                curr_perm.pop()
                available_nums_copy.insert(i, available_nums[i])

        backtrack([], nums)

        return res
