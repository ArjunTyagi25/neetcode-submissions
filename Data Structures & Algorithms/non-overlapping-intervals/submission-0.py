class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])
        count = 0
        cur_end_time = float('-inf')

        for i in range(len(intervals)):
            if cur_end_time <= intervals[i][0]:
                count += 1
                cur_end_time = intervals[i][1]

        return len(intervals) - count
        