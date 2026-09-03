from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)


        @cache
        def dfs(i,j):
            if i == l1:
                return l2 - j
            if j == l2:
                return l1 - i

            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            
            insert = dfs(i + 1, j)
            delete = dfs(i , j+ 1)
            replace = dfs(i + 1, j + 1 )

            return 1 + min(insert, delete, replace)
        return dfs(0,0)