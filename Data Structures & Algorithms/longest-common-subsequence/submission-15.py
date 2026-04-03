class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i == l1 or j == l2:
                return 0
            if text1[i] == text2[j]:
                return dfs(i + 1, j + 1) + 1
            cache[(i,j)] = max(dfs(i + 1, j) , dfs(i , j + 1))
            return cache[(i,j)]
        
        return dfs(0,0)