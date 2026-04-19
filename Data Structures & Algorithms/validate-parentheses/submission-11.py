class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        stack = []

        for i in s:
            # if it's openning, append to stack
            if i in m:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if m[stack[-1]] == i:
                        stack.pop()
                        continue
                    else:
                        print(stack[-1])
                        print(i)
                        return False
        return True if not stack else False