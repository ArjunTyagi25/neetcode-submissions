class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_bracket, close_bracket, curr_string):
            if open_bracket == n and close_bracket == n:
                res.append(curr_string)
                return

            if close_bracket > open_bracket:
                return

            if open_bracket < n:
                curr_string += "("
                backtrack(open_bracket+1, close_bracket, curr_string)
                curr_string = curr_string[:-1]

            if close_bracket < open_bracket:
                curr_string += ")"
                backtrack(open_bracket, close_bracket+1, curr_string)
                curr_string = curr_string[:-1]

        backtrack(0, 0, "")

        return res
        