class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        i, j = 0, 1

        while j != len(s):
            res += abs(ord(s[i]) - ord(s[j]))
            i += 1
            j += 1

        return res
        