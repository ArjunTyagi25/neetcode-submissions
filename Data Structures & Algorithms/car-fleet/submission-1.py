class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []

        for i in range(len(position)):
            pos_speed.append([position[i], speed[i]])

        pos_speed.sort()

        stack = [pos_speed[0]]

        for i in range(1, len(pos_speed)):
            while (stack and ((target - stack[-1][0])/stack[-1][1] <= (target - pos_speed[i][0])/pos_speed[i][1])):
                # Car in stack catches up to the next car so it becomes one fleet
                stack.pop()
            stack.append(pos_speed[i])

        return len(stack)