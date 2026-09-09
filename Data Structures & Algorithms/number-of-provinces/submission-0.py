class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = {i : [] for i in range(len(isConnected))}
        ROWS = len(isConnected)
        COLS = len(isConnected[0])

        for r in range(ROWS):
            for c in range(COLS):
                if r != c and isConnected[r][c] == 1:
                    adj_list[r].append(c)
                    adj_list[c].append(r)
        
        visited = set()

        def dfs(city):
            visited.add(city)
            for neighbor in adj_list[city]:
                if neighbor not in visited:
                    dfs(neighbor)
            
            return

        num_provinces = 0
        for i in range(ROWS):
            if i not in visited:
                num_provinces += 1
                dfs(i)

        return num_provinces

        