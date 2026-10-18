class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [nums[0]] * n
        suffixSum = [nums[-1]] * n

        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1] + nums[i]

        for i in range(n-2, -1, -1):
            suffixSum[i] = suffixSum[i+1] + nums[i]

        for i in range(n):
            if prefixSum[i] == suffixSum[i]:
                return i

        return -1