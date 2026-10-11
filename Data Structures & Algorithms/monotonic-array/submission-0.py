class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if nums[0] <= nums[1]:
            isIncreasing = True
        else:
            isIncreasing = False

        for i in range(1, len(nums) - 1):
            if isIncreasing and nums[i] > nums[i+1]:
                return False
            elif not isIncreasing and nums[i] < nums[i+1]:
                return False

        return True