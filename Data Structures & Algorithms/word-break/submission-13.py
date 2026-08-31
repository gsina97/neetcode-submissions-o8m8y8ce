from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        @cache
        def dfs(i):
            if i == len(s):
                return True
            if i > len(s):
                return False

            
            for w in wordDict:
                if s[i:i + len(w)] == w:
                    if dfs(i + len(w)):
                        return True
            return False
        

        return dfs(0)