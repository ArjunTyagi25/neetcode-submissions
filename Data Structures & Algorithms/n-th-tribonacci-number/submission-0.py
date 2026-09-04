class Solution:
    def tribonacci(self, n: int) -> int:
        memoization = [-1] * (n+1)

        def dfs(i):
            if i == 0:
                return 0
            elif i == 1 or i == 2:
                return 1

            if memoization[i] != -1:
                return memoization[i]

            memoization[i] = dfs(i-1) + dfs(i-2) + dfs(i-3)
            return memoization[i]

        return dfs(n)
        