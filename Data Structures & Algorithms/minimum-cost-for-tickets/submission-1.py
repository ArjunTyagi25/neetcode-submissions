class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def rec(i, pass_valid_day):
            if i == len(days):
                return 0

            if (i, pass_valid_day) in memo:
                return memo[(i, pass_valid_day)]

            if days[i] <= pass_valid_day:
                res = rec(i+1, pass_valid_day)
            else:
                res = min(costs[0] + rec(i+1, -1), costs[1] + rec(i+1, days[i]+6), costs[2] + rec(i+1, days[i]+29))
            
            memo[(i, pass_valid_day)] = res
            return res

        return rec(0, -1)