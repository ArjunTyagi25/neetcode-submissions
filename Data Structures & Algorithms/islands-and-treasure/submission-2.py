class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()

        def nextLand(r, c):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or grid[r][c] == -1 or (r,c) in visited:
                return

            q.append([r,c])
            visited.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                [r,c] = q.popleft()

                grid[r][c] = dist

                nextLand(r+1, c)
                nextLand(r-1, c)
                nextLand(r, c+1)
                nextLand(r, c-1)
            dist += 1

            
        
        