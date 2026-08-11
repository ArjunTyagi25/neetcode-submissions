class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [height[0]] * len(height)
        suffix = [height[-1]] * len(height)
        max_water = 0

        for i in range(1, len(height)):
            prefix[i] = max(prefix[i-1], height[i])

        for i in range(len(height)-2,-1,-1):
            suffix[i] = max(suffix[i+1], height[i])

        for i in range(len(height)):
            max_water += min(prefix[i], suffix[i]) - height[i]

        return max_water  