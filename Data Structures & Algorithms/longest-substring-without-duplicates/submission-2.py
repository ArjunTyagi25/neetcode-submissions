class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        L, R = 0, 1
        window = set(s[L])
        max_length = 1

        while R != len(s):
            # If s[R] is in the window, we shrink the window by removing L's alphabet from the set and incrementing L 
            if s[R] in window:
                window.remove(s[L])
                L += 1
            # If s[R] is not in the window, we add s[R] to the set and increment R by 1, expanding the window
            else:
                window.add(s[R])
                max_length = max(max_length, R-L+1)
                R += 1

        return max_length
        