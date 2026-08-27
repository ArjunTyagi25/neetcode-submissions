class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start_index = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                continue
            else:
                start_index = i
                break

        res = 0
        for i in range(start_index, -1, -1):
            if s[i] != " ":
                res += 1
            else:
                break

        return res
        