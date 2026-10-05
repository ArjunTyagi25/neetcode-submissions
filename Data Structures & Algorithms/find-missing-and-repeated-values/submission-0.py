class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        values = set()
        res = [0, 0]
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] in values:
                    res[0] = grid[r][c]
                else:
                    values.add(grid[r][c])

        for i in range(1, ROWS*COLS+1):
            if i not in values:
                res[1] = i

        return res
        
        