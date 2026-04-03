class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for i in s:
            if i in mapping:
                if not stack:
                    return False
                if stack.pop() != mapping[i]:
                    return False
            else:
                stack.append(i)

        return True if not stack else False