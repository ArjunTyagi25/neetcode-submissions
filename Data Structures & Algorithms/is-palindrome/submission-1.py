class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_no_spaces = []

        for i in range(len(s)):
            if 48 <= ord(s[i]) <= 57 or 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122:
                s_no_spaces.append(s[i].lower())

        L, R = 0, len(s_no_spaces) - 1

        while L < R:
            if s_no_spaces[L] != s_no_spaces[R]:
                return False
            L += 1
            R -= 1

        return True
        