class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        N = len(mat)
        for i in range(N):
            res += mat[i][i]
            res += mat[i][N-i-1]

        if N%2 != 0:
            res -= mat[N//2][N//2]
        return res

        