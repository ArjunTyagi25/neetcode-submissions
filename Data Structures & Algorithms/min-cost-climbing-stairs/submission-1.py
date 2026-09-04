class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memoization = [-1] * len(cost) # Maps each step to min cost required to reach that step
        def dfs(i):
            if i >= len(cost):
                return 0

            if memoization[i] != -1:
                return memoization[i]

            memoization[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memoization[i]

        return min(dfs(0), dfs(1))