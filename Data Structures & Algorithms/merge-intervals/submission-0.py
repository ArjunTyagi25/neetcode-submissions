class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        res = []
        i = 0

        while i <= len(intervals)-1:
            res.append(intervals[i])
            i += 1
            while i <= len(intervals)-1 and res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
                i += 1

        return res