class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r, c, prev_height, curr_set):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or (r,c) in curr_set or heights[r][c] < prev_height:
                return

            curr_set.add((r,c))
            dfs(r-1, c, heights[r][c], curr_set)
            dfs(r+1, c, heights[r][c], curr_set)
            dfs(r, c-1, heights[r][c], curr_set)
            dfs(r, c+1, heights[r][c], curr_set)

        pac, atl = set(), set()
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS-1, heights[r][COLS-1], atl)

        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS-1, c, heights[ROWS-1][c], atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
            
        