class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = {}
        for c in s:
            s_freq[c] = 1 + s_freq.get(c, 0)

        t_freq = {}
        for c in t:
            t_freq[c] = 1 + t_freq.get(c, 0)

        if s_freq == t_freq:
            return True
        else:
            return False