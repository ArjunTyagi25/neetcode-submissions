class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or (r,c) in visited or grid[r][c] == 0:
                return

            grid[r][c] = -1
            q.append((r,c))
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
            return

        found = False
        for r in range(ROWS):
            if found:
                break
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r,c)
                    found = True
                    break

        res = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for nr, nc in [[1,0], [0,1], [-1,0], [0,-1]]:
                    dr, dc = r+nr, c+nc

                    if 0 <= dr < ROWS and 0 <= dc < COLS and (dr,dc) not in visited:
                        if grid[dr][dc] == 1:
                            return res

                        if grid[dr][dc] == 0:
                            grid[dr][dc] = -1
                            q.append((dr,dc))
                            visited.add((dr,dc))
            res += 1

        return res    
