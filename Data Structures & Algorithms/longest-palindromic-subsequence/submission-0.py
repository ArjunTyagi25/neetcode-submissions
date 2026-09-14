class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def rec(L, R):
            if L > R:
                return 0
            
            if L == R:
                return 1

            if (L,R) in memo:
                return memo[(L,R)]

            if s[L] == s[R]:
                memo[(L,R)] = 2 + rec(L+1, R-1)
            else:
                memo[(L,R)] = max(rec(L+1, R), rec(L, R-1))
                
            return memo[(L,R)]

        return rec(0, len(s)-1)
        