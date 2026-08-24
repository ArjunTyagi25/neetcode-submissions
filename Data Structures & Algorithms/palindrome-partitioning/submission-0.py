class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        par = []

        def backtrack(i):
            if i == len(s):
                res.append(par.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    par.append(s[i:j+1])
                    backtrack(j+1)
                    par.pop()

        backtrack(0)

        return res

    def isPalindrome(self, s, i, j):
        while i<=j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True
        