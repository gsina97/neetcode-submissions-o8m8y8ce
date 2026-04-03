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

                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop()+  digit  
                
                stack.append(int(digit) * subarr)
        
        return "".join(stack)