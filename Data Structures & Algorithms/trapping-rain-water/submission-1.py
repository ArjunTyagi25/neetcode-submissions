class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [height[0]] * n
        suffix = [height[-1]] * n

        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i])

        for i in range(n-2,-1,-1):
            suffix[i] = max(suffix[i+1], height[i])

        total_water = 0
        for i in range(n):
            total_water += (min(prefix[i], suffix[i]) - height[i])

        return total_water 