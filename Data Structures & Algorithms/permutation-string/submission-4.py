class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = {chr(i): 0 for i in range(ord('a'), ord('z')+1)} 
        window = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
        for i in range(len(s1)):
            count[s1[i]] += 1
            window[s2[i]] += 1

        if window == count:
            return True

        L = 0
        for R in range(len(s1), len(s2)):
            window[s2[L]] -= 1
            L += 1
            window[s2[R]] += 1

            if count == window:
                return True

        return False



        