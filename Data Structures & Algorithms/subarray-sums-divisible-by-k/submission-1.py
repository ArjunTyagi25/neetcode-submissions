class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Brute force: O(N^2)
        res = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i+1, len(nums)+1):
                total = total + nums[j-1]
                if total % k == 0:
                    res += 1

        return res