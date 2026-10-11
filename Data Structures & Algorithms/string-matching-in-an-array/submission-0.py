class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        allSubstrings = set()

        for word in words:
            for i in range(len(word)):
                for j in range(i+1, len(word)+1):
                    if word[i:j] != word:
                        allSubstrings.add(word[i:j])

        res = []
        for word in words:
            if word in allSubstrings:
                res.append(word)

        return res