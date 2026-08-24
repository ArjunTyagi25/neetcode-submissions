class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(perm, available_nums):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return 

            for i in range(len(available_nums)):
                available_nums_copy = available_nums.copy()

                num = available_nums_copy[i]

                perm.append(num)
                available_nums_copy.pop(i)

                dfs(perm, available_nums_copy)

                available_nums_copy.insert(i, num)
                perm.pop()

        dfs([], nums)

        return res