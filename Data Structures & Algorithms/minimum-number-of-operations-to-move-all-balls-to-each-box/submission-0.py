class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxesWithBalls = set()

        for i in range(len(boxes)):
            if boxes[i] == "1":
                boxesWithBalls.add(i)

        res = []
        for i in range(len(boxes)):
            numOps = 0

            for j in boxesWithBalls:
                numOps += abs(i-j)

            res.append(numOps)

        return res