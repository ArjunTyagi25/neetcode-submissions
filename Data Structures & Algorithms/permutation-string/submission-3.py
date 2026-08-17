class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for s in s1:
            s1_count[s] = 1 + s1_count.get(s, 0)

        have, need = 0, len(s1_count)
        L = 0

        s2_count = {}
        for R in range(len(s2)):
            if s2[R] not in s1_count.keys():
                L = R + 1
                s2_count = {}
                have = 0
            else:
                s2_count[s2[R]] = 1 + s2_count.get(s2[R], 0)
                if (s2_count[s2[R]] == s1_count[s2[R]]):
                    have += 1
                elif (s2_count[s2[R]] > s1_count[s2[R]]):
                    while (L<=R and s2_count[s2[R]] > s1_count[s2[R]]):
                        s2_count[s2[L]] -= 1
                        if s2_count[s2[L]] < s1_count[s2[L]]:
                            have -= 1
                        L += 1
                
                if (have == need):
                    return True

        return False



        