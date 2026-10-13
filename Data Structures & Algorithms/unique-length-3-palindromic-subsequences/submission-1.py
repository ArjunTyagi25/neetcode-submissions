class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0

        for i in range(97, 123):
            first, last = -1, -1

            for j in range(len(s)):
                if s[j] == chr(i):
                    if first == -1:
                        first = j
                    last = j
            
            if first != last:
                distinctChars = set()

                for j in range(first+1, last):
                    distinctChars.add(s[j])

                res += len(distinctChars)

        return res