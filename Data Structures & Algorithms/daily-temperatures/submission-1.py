class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [temperatures[0]]
        indices = [0]
        res = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            temp = temperatures[i]

            if stack[-1] < temp:
                while (stack and stack[-1] < temp):
                    idx = indices[-1]
                    res[idx] = i - idx

                    indices.pop()
                    stack.pop()

                stack.append(temp)
                indices.append(i)
            else:
                stack.append(temp)
                indices.append(i)

        return res


# [70, 69, 68, 67, 80]

# stack = [80]
# indices = [4]