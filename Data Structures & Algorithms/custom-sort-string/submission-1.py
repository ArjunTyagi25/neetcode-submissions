class Solution:
    def customSortString(self, order: str, s: str) -> str:
        countS = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)

        res = []
        for c in order:
            if c in countS:
                res.append(c * countS[c])
                del countS[c]
            
        for k, v in countS.items():
                res.append(k * v)

        return ''.join(res)