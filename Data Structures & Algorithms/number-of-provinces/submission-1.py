class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS = len(isConnected)
        COLS = len(isConnected[0])
        adjList = { i : [] for i in range(ROWS)}
        
        for r in range(ROWS):
            for c in range(COLS):
                if r != c and isConnected[r][c] == 1:
                    adjList[r].append(c)
                    adjList[c].append(r)

        visited = set()
        def dfs(i):

            for neighbor in adjList[i]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

            return

        numProvinces = 0
        for i in range(ROWS):
            if i not in visited:
                numProvinces += 1
                dfs(i)

        return numProvinces

        