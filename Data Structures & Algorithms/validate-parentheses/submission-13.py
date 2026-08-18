class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False

        
        stack = []
        mapping = {"{" : "}","(" : ")","[" : "]"}

        for char in s:
            # if openning continue
            if char in mapping:
                stack.append(char)
            else:
                # if closed, need to check and if valid pop
                if stack and mapping[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        
        return stack == []
            