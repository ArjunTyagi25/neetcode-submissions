class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}

        def rec(startIndex):
            if startIndex == len(s):
                return True

            if startIndex in memo:
                return memo[startIndex]

            for endIndex in range(startIndex+1, len(s)+1):
                if s[startIndex : endIndex] in wordDict and rec(endIndex):
                    memo[startIndex] = True
                    return True

            memo[startIndex] = False
            return False

        return rec(0)
        