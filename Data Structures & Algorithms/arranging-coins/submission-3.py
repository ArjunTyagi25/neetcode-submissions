class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
            
        L, R = 0, n

        while L<R:
            M = (L+R)//2

            if M*(M+1)/2 > n:
                R = M
            else:
                L = M + 1

        return R-1
        