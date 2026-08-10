class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] in ['[','{','(']:
                stack.append(s[i])
            elif s[i] in [']','}',')']:
                if stack == []:
                    return False
                else:
                    matching_bracket = stack.pop()

                if s[i] == ']' and matching_bracket != '[':
                    return False
                elif s[i] == '}' and matching_bracket != '{':
                    return False
                elif s[i] == ')' and matching_bracket != '(':
                    return False

        if stack != []:
            return False

        return True
        