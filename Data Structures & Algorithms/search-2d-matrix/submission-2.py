class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix)-1
        row = -1

        while L <= R:
            M = (L+R)//2

            if target < matrix[M][0]:
                R = M - 1
            elif target > matrix[M][-1]:
                L = M + 1
            else:
                row = M
                break

        L, R = 0, len(matrix[row])-1

        while L <= R:
            M = (L+R)//2

            if matrix[row][M] < target:
                L = M + 1
            elif matrix[row][M] > target:
                R = M - 1
            else:
                return True

        return False

        
# target = 3
#         R
#  L  R
# [1, 3]