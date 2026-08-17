import string

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_freq = {}
        for c in t:
            target_freq[c] = 1 + target_freq.get(c, 0)

        need = len(target_freq)
        have = 0
        window_freq = {}
        L = 0
        res, res_length = [-1,-1], float('inf')

        for R in range(len(s)):
            # Add new character to window hash map
            window_freq[s[R]] = 1 + window_freq.get(s[R], 0)

            # If that character is part of t, check if we meet the target frequency and if so, increment have
            if (s[R] in target_freq and window_freq[s[R]] == target_freq[s[R]]):
                have += 1

            # If we have all the characters and their frequencies that we need, keep shrinking the window till have is not equal to need
            while (have == need):
                if R-L+1 < res_length:
                    res_length = R-L+1
                    res = [L,R]

                window_freq[s[L]] -= 1
                if (s[L] in target_freq and window_freq[s[L]] < target_freq[s[L]]):
                    have -= 1
                L += 1

        if res == [-1,-1]:
            return ""
        else:
            return s[res[0] : res[1]+1]

        
        
        