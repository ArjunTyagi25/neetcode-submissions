class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        minCount = [float('inf')] * 26

        for word in words:
            wordCount = [0] * 26

            for c in word:
                wordCount[ord(c) - 97] += 1

            for i in range(26):
                minCount[i] = min(minCount[i], wordCount[i])

        res = []
        for i in range(26):
            if minCount[i] != 0:
                for j in range(minCount[i]):
                    res.append(chr(i+97))

        return res