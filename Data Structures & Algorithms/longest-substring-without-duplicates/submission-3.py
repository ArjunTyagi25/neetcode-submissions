class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_length = 0
        L = 0

        for R in range(len(s)):
            if s[R] in window:
                while len(window) != 0 and s[R] in window:
                    window.remove(s[L])
                    L += 1
            window.add(s[R])
            max_length = max(max_length, len(window))

        return max_length
        