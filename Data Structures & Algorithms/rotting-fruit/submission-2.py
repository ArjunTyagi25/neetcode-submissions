class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        self.freshFruits = 0

        def addFruit(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r,c) in visited:
                return

            q.append((r,c))
            visited.add((r,c))
            self.freshFruits -= 1


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    self.freshFruits += 1

        res = 0
        while q and self.freshFruits > 0:
            for i in range(len(q)):
                (r, c) = q.popleft()

                grid[r][c] = 2
                visited.add((r, c))

                addFruit(r + 1, c)
                addFruit(r - 1, c)
                addFruit(r, c + 1)
                addFruit(r, c - 1)
            
            if q:
                res += 1

        return res if self.freshFruits == 0 else -1