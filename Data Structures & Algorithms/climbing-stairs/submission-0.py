class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        last_two_steps = [1, 2]
        i = 2

        while i <= n:
            temp = last_two_steps[1]
            last_two_steps[1] = last_two_steps[0] + last_two_steps[1]
            last_two_steps[0] = temp
            i += 1

        return last_two_steps[0]
        