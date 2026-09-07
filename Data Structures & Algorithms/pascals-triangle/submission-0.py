class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * i for i in range(1, numRows+1)]

        if numRows <= 2:
            return res

        for r in range(2, numRows):
            for i in range(1, r):
                res[r][i] = res[r-1][i-1] + res[r-1][i]

        return res


'''
numRows = 4             len     r
        1               1       0
      1   1             2       1   
    1   2   1           3       2   
  1   3   3   1         4       3
'''
        