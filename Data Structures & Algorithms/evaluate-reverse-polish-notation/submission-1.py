import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul
        }
        for val in tokens:
            if val in {"-", "+", "/", "*"}:
                b = stack.pop()
                a = stack.pop()
                if val == "/":
                    result = abs(a) // abs(b)
                    if a * b < 0:
                        result = -result
                    stack.append(result)
                else:
                    result = operators[val](a, b)
                    stack.append(result)
            else:
                stack.append(int(val))
        return stack[-1]