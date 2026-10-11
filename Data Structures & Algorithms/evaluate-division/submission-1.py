class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = {}

        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]

            if a not in adjList:
                adjList[a] = []
            adjList[a].append((b, val))

            if b not in adjList:
                adjList[b] = []
            adjList[b].append((a, 1/val))

        def dfs(node, dst, currPath, runningValue):
            if node == dst:
                return [True, runningValue] # [Found, Value]

            currPath.add(node)
            for nextNode, val in adjList[node]:
                if nextNode not in currPath:
                    found, total = dfs(nextNode, dst, currPath, runningValue * val)
                    if found:
                        return [True, total]

            return [False, -1] 

        res = []
        for src, dst in queries:
            if src not in adjList:
                res.append(-1)
            else:
                found, val = dfs(src, dst, set(), 1)
                if found:
                    res.append(val)
                else:
                    res.append(-1)

        return res