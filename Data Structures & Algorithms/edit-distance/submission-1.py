class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def rec(i, j):
            if i == len(word1) and j != len(word2):
                return len(word2) - j
            elif i != len(word1) and j == len(word2):
                return len(word1) - i
            elif i == len(word1) and j == len(word2):
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            if word1[i] == word2[j]:
                return rec(i+1, j+1)

            res = 1 + min(rec(i, j+1), rec(i+1, j), rec(i+1, j+1))
            memo[(i,j)] = res
            return res

        return rec(0, 0)
        