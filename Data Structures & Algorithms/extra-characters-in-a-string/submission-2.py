class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wordDictionary = set(dictionary)
        memo = {}
        def rec(i):
            if i == len(s):
                return 0

            if i in memo:
                return memo[i]

            res = 1 + rec(i+1)

            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDictionary:
                    res = min(res, rec(j))

            memo[i] = res
            return res

        return rec(0)
        