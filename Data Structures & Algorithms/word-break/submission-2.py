class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict_set = set(wordDict)
        index_to_value = {}

        def dfs(i):
            if i == len(s):
                return True

            for j in range(i, len(s)):
                if s[i:j+1] in wordDict_set:
                    if j+1 in index_to_value:
                        if index_to_value[j+1]:
                            return True
                    else:
                        res = dfs(j+1)
                        index_to_value[j+1] = res
                        if res:
                            return True
            return False

        return dfs(0)