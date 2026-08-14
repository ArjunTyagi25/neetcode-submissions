class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = float('-inf')
        L, R = 0, len(heights)-1

        while L<R:
            h = min(heights[L], heights[R])
            max_area = max(max_area, h * (R-L))

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return max_area