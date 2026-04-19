class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                b = int(stack.pop())
                a = int(stack.pop())
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "/":
                    stack.append(int(a/b))
                else:
                    stack.append(a*b)
            else:
                stack.append(int(t))
        return stack[0]

        