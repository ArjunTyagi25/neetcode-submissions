import string

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_freq = {}
        for alphabet in t:
            t_freq[alphabet] = 1 + t_freq.get(alphabet, 0)
        need = len(t_freq.keys())

        window_freq = {}
        have = 0

        res, res_length = [-1, -1], float('inf')
        L = 0

        for R in range(len(s)):
            window_freq[s[R]] = 1 + window_freq.get(s[R], 0)

            if (s[R] in t_freq.keys() and window_freq[s[R]] == t_freq[s[R]]):
                have += 1

            while (have == need):
                # update res and res_length
                if (R - L + 1) < res_length:
                    res = [L, R]
                    res_length = R - L + 1
                
                # pop one element from the left of the window
                window_freq[s[L]] -= 1
                if (s[L] in t_freq.keys() and window_freq[s[L]] < t_freq[s[L]]):
                    have -= 1
                L += 1

        if res == [-1,-1]:
            return ""
        else:
            return s[res[0] : res[1]+1]
        
        