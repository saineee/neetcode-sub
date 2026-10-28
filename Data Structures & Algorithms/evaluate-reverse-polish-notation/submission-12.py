import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        lookup = {
            "*": operator.mul,
            "-": operator.sub,
            "+": operator.add
        }
        for char in tokens:
            if char in {"*", "/", "+", "-"}:
                val_b = stack.pop()
                val_a = stack.pop()
                if char == "/":
                    res = (abs(val_a) // abs(val_b))
                    if val_a * val_b < 0:
                        res = -res
                else:
                    res = lookup[char](val_a, val_b)
                stack.append(res)
            else:
                stack.append(int(char))

        return stack[-1]