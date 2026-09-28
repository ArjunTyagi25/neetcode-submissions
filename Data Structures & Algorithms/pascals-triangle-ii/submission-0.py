class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        prevRow = [1]
        row = 0

        while row != rowIndex+1:
            nextRow = [1] * (row+1)

            for r in range(1, len(nextRow)-1):
                nextRow[r] = prevRow[r-1] + prevRow[r]

            prevRow = nextRow
            row += 1

        return prevRow
        