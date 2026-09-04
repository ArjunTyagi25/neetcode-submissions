class Solution:
    def rob(self, nums: List[int]) -> int:
        index_to_value = {}

        def rec(i):
            if i >= len(nums):
                return 0
            
            if i in index_to_value:
                return index_to_value[i]

            index_to_value[i] = max(nums[i] + rec(i+2), rec(i+1))
            return index_to_value[i]

        return rec(0)
        