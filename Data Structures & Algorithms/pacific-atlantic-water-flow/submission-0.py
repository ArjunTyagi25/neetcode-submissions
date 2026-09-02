class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacs, atl = set(), set()

        def dfs(r, c, visit, prev_height):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or prev_height > heights[r][c]:
                return

            visit.add((r, c))

            dfs(r-1, c, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])


        # Running DFS from every Pacific border cell
        for r in range(ROWS):
            dfs(r, 0, pacs, 0)
        for c in range(COLS):
            dfs(0, c, pacs, 0)

        # Running DFS from every Atlantic border cell
        for r in range(ROWS):
            dfs(r, COLS - 1, atl, 0)
        for c in range(COLS):
            dfs(ROWS - 1, c, atl, 0)

        res = []
        # Check if each cell in present in both pacs and atl
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacs and (r,c) in atl:
                    res.append([r, c])

        return res
        