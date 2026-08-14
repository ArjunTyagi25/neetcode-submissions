class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            length = len(s)
            res = res + str(length) + "$" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i != len(s):
            length = ""
            while s[i] != "$":
                length = length + s[i]
                i += 1
            i += 1

            length = int(length)
            stop_index = i + length
            
            word = ""
            while i < stop_index:
                word = word + s[i]
                i += 1

            res.append(word)

        return res





