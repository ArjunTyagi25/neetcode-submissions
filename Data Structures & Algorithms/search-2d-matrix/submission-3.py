class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_start, row_end = 0, len(matrix)-1

        while row_start<=row_end:
            row_mid = (row_start+row_end)//2

            if matrix[row_mid][0] > target:
                row_end = row_mid - 1
            elif matrix[row_mid][-1] < target:
                row_start = row_mid + 1
            else:
                break

        L, R = 0, len(matrix[row_mid])-1

        while L<=R:
            M = (L+R)//2

            if matrix[row_mid][M] < target:
                L = M + 1
            elif matrix[row_mid][M] > target:
                R = M - 1
            else:
                return True
        
        return False
        