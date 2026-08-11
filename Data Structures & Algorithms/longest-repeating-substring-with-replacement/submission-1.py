class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {chr(i): 0 for i in range(ord('A'),ord('Z')+1,1)}
        max_length = 0
        L, R = 0, 0

        while R != len(s):
            print(L, R)
            frequency[s[R]] += 1
            maxCount = max(frequency.values())

            if ((R - L + 1) - maxCount > k):
                frequency[s[L]] -= 1
                L += 1

            max_length = max(max_length, R-L+1)
            R += 1

        return max_length

        