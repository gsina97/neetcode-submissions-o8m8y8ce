from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        @cache
        def dfs(r,c):
            if r == 0 or c == 0:
                return 1
            

            res = dfs(r - 1, c) + dfs(r, c - 1)
            return res
        

        return dfs(m - 1, n - 1)