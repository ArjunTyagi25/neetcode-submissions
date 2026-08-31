class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_non_zeroes = 0
        for num in nums:
            if num != 0:
                count_non_zeroes += 1

        i = 0
        while i < count_non_zeroes:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1

            
        