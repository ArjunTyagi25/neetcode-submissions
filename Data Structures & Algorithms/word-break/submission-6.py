class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict_set = set(wordDict)
        memo = {}

        def dfs(start_index):
            if start_index == len(s):
                return True

            if start_index in memo:
                return memo[start_index]

            for end_index in range(start_index+1, len(s)+1):
                substring = s[start_index:end_index]

                if substring in wordDict_set:
                    if end_index in memo and memo[end_index]:
                        return True
                    else:
                        memo[end_index] = dfs(end_index)
                        if memo[end_index]:
                            return True

            memo[start_index] = False
            return False

        return dfs(0)