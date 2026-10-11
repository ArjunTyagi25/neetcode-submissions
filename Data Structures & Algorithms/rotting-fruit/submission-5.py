class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        num_fresh_fruits = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh_fruits += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))

        if num_fresh_fruits == 0:
            return 0

        time = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr > ROWS-1 or nc > COLS-1 or grid[nr][nc] != 1 or (nr,nc) in visited:
                        continue
                    
                    grid[nr][nc] = 2
                    num_fresh_fruits -= 1
                    q.append((nr, nc))
                    visited.add((nr, nc))

            time += 1

        if num_fresh_fruits != 0:
            return -1
        return time