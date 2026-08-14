class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] in ['(','{','[']:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                
                opening_bracket = stack.pop(-1)
                if s[i] == ')' and opening_bracket != '(':
                    return False
                elif s[i] == '}' and opening_bracket != '{':
                    return False
                elif s[i] == ']' and opening_bracket != '[':
                    return False

        if len(stack) != 0:
            return False

        return True


        