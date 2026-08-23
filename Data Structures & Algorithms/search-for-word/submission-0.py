class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, i):
            if i == len(word):
                return True
            
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or visited[row][col]:
                return False
            elif board[row][col] != word[i]:
                return False

            visited[row][col] = True
            if dfs(row+1, col, i+1) or dfs(row, col+1, i+1) or dfs(row-1, col, i+1) or dfs(row, col-1, i+1):
                res = True
            else:
                res = False

            visited[row][col] = False

            return res
            
        visited = []
        for r in range(len(board)):
            row_visit = []
            for c in range(len(board[0])):
                row_visit.append(False)
            visited.append(row_visit)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
    
        return False

        