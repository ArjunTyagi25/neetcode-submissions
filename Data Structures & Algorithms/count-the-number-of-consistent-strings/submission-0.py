class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        res = 0

        for word in words:
            word_set = set(word)

            if word_set <= allowed_set:
                res += 1

        return res

        