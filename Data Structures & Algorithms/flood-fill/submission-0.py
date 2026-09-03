class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        original_color = image[sr][sc]
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or (r,c) in visited or image[r][c] != original_color:
                return

            visited.add((r,c))
            image[r][c] = color

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)

        return image




