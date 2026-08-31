class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, res = 0, 0

        while i != len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
                res += 1

        return res+1

        