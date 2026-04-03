class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                subNum = ""
                while stack and stack[-1].isdigit():
                    subNum = stack.pop() + subNum
                stack.append(int(subNum) * substr)
        return "".join(stack)
