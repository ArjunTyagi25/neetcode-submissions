class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        zero_indices = []

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_indices.append(i)
            else:
                prod *= nums[i]

        res = [prod] * len(nums)

        for i in range(len(nums)):
            if zero_indices == []:
                res[i] = int(res[i]/nums[i])
            elif len(zero_indices) == 1:
                if i not in zero_indices:
                    res[i] = 0
            else:
                res[i] = 0

        return res
        