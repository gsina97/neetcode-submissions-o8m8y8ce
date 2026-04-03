class Solution:
    def decodeString(self, s: str) -> str:
        stack = []


        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                subarr = ""
                while stack[-1] != "[":
                    subarr = stack.pop() + subarr
                stack.pop()

                digits = ""
                while stack and stack[-1].isdigit():
                    digits = stack.pop() + digits
                
                stack.append(int(digits) * subarr)
        return "".join(stack)