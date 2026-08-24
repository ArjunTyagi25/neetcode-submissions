class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if not digits:
            return res

        hash_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrace(i, curr_comb):
            if i == len(digits):
                res.append(curr_comb)
                return

            chars = hash_map[digits[i]]

            for c in chars:
                backtrace(i+1, curr_comb + c)

        backtrace(0, "")        

        return res