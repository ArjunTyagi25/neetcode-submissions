class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_freq = {chr(i): 0 for i in range(ord('a'), ord('z')+1, 1)}
        for s in s1:
            s1_freq[s] += 1

        window_freq = {chr(i): 0 for i in range(ord('a'), ord('z')+1, 1)}
        for s in s2[0:len(s1)]:
            window_freq[s] += 1

        R = len(s1)-1

        for L in range(len(s2) - len(s1) + 1):
            if window_freq == s1_freq:
                return True
            else:
                window_freq[s2[L]] -= 1
                if R != len(s2)-1:
                    R += 1
                    window_freq[s2[R]] += 1

        return False
        
        