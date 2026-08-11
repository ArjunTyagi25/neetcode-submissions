class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [[0, heights[0]]]
        max_area = 0

        for i in range(1, len(heights)):
            if (heights[i] >= stack[-1][1]):
                stack.append([i, heights[i]])
            else:
                pop_count = 0
                while (stack and (heights[i] < stack[-1][1])):
                    max_area = max(max_area, stack[-1][1] * (i - stack[-1][0]))
                    start_index = stack[-1][0]
                    stack.pop()

                stack.append([start_index, heights[i]])

        while stack:
            max_area = max(max_area, (len(heights) - stack[-1][0]) * stack[-1][1])
            stack.pop()

        return max_area

        