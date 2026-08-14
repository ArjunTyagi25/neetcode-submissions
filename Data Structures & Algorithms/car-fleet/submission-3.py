class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(speed)):
            pos_speed.append([position[i], speed[i]])

        pos_speed.sort(key = lambda x: x[0])

        res = [pos_speed[0]]

        for i in range(1, len(pos_speed)):
            while len(res) != 0 and (target - pos_speed[i][0])/pos_speed[i][1] >= (target - res[-1][0])/res[-1][1]:
                res.pop()

            res.append(pos_speed[i])

        return len(res)
        