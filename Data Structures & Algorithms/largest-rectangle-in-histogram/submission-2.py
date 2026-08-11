class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        We maintain a monotonically increasing stack of <start_index, height> where start index representing the index value at which height can begin. As we iterate through each bar, we check if the current bar's height is greater than the largest bar we got in the stack (largest bar will be at the top since the stack is monotonically increasing). If true, we add the current index (representing the index at which current bar's height begin) and current bar's height to the stack. Otherwise, we do the following:
        - We update the max area based on the largest bar in the stack, followed by popping it.
        - We keep doing this till the bar at the top of the stack is smaller than the current bar
        - Once that is the case, we add the current bar's height along with the index of the last popped bar. That is the because that index represents the left boundary for the current bar's height, since the bar in the stack is smaller than the current bar.

        Once we have iterated through all the bar, we then iterate through the remaining elements in the stack to update the max area.
        """
        stack = [[0, heights[0]]]
        max_area = 0

        for i in range(1, len(heights)):
            if (heights[i] >= stack[-1][1]):
                stack.append([i, heights[i]])
            else:
                while (stack and (heights[i] < stack[-1][1])):
                    max_area = max(max_area, stack[-1][1] * (i - stack[-1][0]))
                    start_index = stack[-1][0]
                    stack.pop()

                stack.append([start_index, heights[i]])

        while stack:
            max_area = max(max_area, (len(heights) - stack[-1][0]) * stack[-1][1])
            stack.pop()

        return max_area

        