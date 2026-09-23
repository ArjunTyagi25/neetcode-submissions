class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        transpose_matrix = [[0] * ROWS for _ in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS):
                transpose_matrix[c][r] = matrix[r][c]

        return transpose_matrix
        