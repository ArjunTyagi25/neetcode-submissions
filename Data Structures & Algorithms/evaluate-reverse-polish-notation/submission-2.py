class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(token)
            else:
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())

                if token == "+":
                    res = operand_1 + operand_2
                elif token == "-":
                    res = operand_1 - operand_2
                elif token == "*":
                    res = operand_1 * operand_2
                elif token == "/":
                    res = operand_1 / operand_2

                stack.append(res)
        
        return int(stack[0])