class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        for i in range(n):
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i, newInterval)

        if len(intervals) == n:
            intervals.append(newInterval)

        res = []
        i = 0
        while i <= len(intervals)-1:
            res.append(intervals[i])
            i += 1
            while i < len(intervals) and res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
                i += 1

        return res