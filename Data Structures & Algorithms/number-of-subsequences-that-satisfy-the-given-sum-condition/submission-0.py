class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        i, j = 0, len(nums) - 1
        mod = 10**9 + 7

        while i<=j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                res += pow(2, j-i)
                i += 1
        
        return res%mod

        