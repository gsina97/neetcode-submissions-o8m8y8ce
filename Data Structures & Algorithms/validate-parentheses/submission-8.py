class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        stack = []

        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if stack and mapping[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False