class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGapAtIndex = {0:0}

        for r in wall:
            total = 0
            for i in range(len(r) - 1):
                total += r[i]
                countGapAtIndex[total] = 1 + countGapAtIndex.get(total, 0)

        return len(wall) - max(countGapAtIndex.values())
        