class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for i in range(len(s)):
            if s[i].isalnum():
                chars.append(s[i])

        L, R = 0, len(chars)-1
        while L <= R:
            if chars[L].lower() != chars[R].lower():
                return False

            L = L + 1
            R = R - 1

        return True
        