class Solution:
    def customSortString(self, order: str, s: str) -> str:
        countS = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)

        res = ""
        for c in order:
            if c in countS:
                res = res + c * countS[c]
                countS[c] = 0
            
        for k, v in countS.items():
            if v != 0:
                res = res + k * v
                countS[k] = 0

        return res