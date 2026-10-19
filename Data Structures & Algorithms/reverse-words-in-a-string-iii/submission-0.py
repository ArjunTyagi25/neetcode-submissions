class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        word = []
        for c in s:
            if c == " ":
                while word:
                    res = res + word[-1]
                    word.pop()
                res += " "
            else:
                word.append(c)

        while word:
            res = res + word[-1]
            word.pop()

        return res
