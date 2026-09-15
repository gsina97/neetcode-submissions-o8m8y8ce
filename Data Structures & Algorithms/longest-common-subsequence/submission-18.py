
from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        p1 = 0
        p2 = 0
        l1 = len(text1)
        l2 = len(text2)

        @cache         
        def dfs(p1, p2):
            if p1 == l1 and p2 == l2:
                return 0
            if p1 == l1:
                return dfs(p1, p2 + 1)
            if p2 == l2:
                return dfs(p1 + 1, p2)
            
            if text1[p1] == text2[p2]:
                return 1 + dfs(p1+1, p2 + 1)
            else:
                return  max(dfs(p1 + 1, p2), dfs(p1 , p2 + 1))
            


        return dfs(0,0)            