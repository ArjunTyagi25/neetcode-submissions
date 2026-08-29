class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def recursion(i, total):
            if i == len(nums):
                return total

            return recursion(i+1, total ^ nums[i]) + recursion(i+1, total)
        
        return recursion(0, 0)
            

             
        