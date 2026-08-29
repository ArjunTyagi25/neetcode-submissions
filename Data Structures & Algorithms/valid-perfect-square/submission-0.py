class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def checkSquare(n):
            if n*n > num:
                return 1
            elif n*n < num:
                return -1
            else:
                return 0

        L, R = 1, num

        while L<=R:
            M = (L+R)//2

            if checkSquare(M) == 1:
                R = M - 1
            elif checkSquare(M) == -1:
                L = M + 1
            else:
                return True

        return False
        