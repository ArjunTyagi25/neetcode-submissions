class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)

        res = 0
        for word in words:
            hash_map = Counter(word)

            if hash_map <= char_count:
                res += len(word)

        return res
        