class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        for c in s:
            # if closing bracket
            if c in pairs.keys():
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return not stack


