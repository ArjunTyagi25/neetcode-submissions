class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree, outdegree = [0] * n, [0] * n

        for s, d in trust:
            outdegree[s-1] += 1
            indegree[d-1] += 1

        for i in range(n):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i+1

        return -1
