class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [[temperatures[0],0]]
        res = [0] * len(temperatures)
        i = 1

        for i in range(len(temperatures)):
            
            while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i], i])

        return res



        