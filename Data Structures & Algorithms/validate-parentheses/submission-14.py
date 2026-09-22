class Solution:
    def isValid(self, s: str) -> bool:
        stack = []


        mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
            }

        
        for n in s:
            # opening
            if n not in mapping:
                stack.append(n)
                print("here1")
            else:
                # close
                if stack:
                    # closing mast match withj top stack open
                    # mappijng(]) == [
                    print("here2")
                    
                    if mapping[n] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    print("here3", n)
                    return False
        return True if not stack else False
        