class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.perimeter = 0

        def dfs(r, c, visited):
            ROWS, COLS = len(grid), len(grid[0])
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                self.perimeter += 1
                return

            if (r,c) in visited:
                return

            visited.add((r,c))
            dfs(r-1, c, visited)
            dfs(r+1, c, visited)
            dfs(r, c-1, visited)
            dfs(r, c+1, visited)

            return

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r, c, set())
                    return self.perimeter
        