class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen_integers = set()

        for i in range(len(nums)):
            if nums[i] not in seen_integers:
                seen_integers.add(nums[i])
            else:
                return nums[i]
        