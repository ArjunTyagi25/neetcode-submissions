class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        L = 0
        hash_map = {}

        for R in range(len(s)):
            hash_map[s[R]] = 1 + hash_map.get(s[R], 0)
            max_count = max(hash_map.values())

            if (R - L + 1 - max_count) > k:
                hash_map[s[L]] -= 1
                L += 1

            res = max(res, R-L+1)

        return res
        