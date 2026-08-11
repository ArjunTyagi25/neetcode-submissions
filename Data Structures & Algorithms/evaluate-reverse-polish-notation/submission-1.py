class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                operand_2 = int(stack.pop())
                operand_1 = int(stack.pop())
                
                if token is "+":
                    val = operand_1 + operand_2
                elif token is "-":
                    val = operand_1 - operand_2
                elif token is "*":
                    val = operand_1 * operand_2
                elif token is "/":
                    val = operand_1 / operand_2
                
                stack.append(val)
            else:
                stack.append(token)

        return int(stack[0])
        