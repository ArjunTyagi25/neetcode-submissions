class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        chars = ['b','a','l','o','n']

        for s in text:
            if s in chars:
                freq[s] += 1

        res = 0
        while freq['b'] > 0 and freq['a'] > 0 and freq['l'] > 0 and freq['o'] > 0 and freq['n'] > 0:
            freq['b'] -= 1
            freq['a'] -= 1
            freq['l'] -= 2
            freq['o'] -= 2
            freq['n'] -= 1

            if (freq['b'] >= 0 and freq['a'] >= 0 and freq['l'] >= 0 and freq['o'] >= 0 and freq['n'] >= 0):
                res += 1

        return res

        