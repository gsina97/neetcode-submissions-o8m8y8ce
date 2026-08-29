class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = {}
        def dfs(r,c):
            if (r,c) in cache:
                return cache[(r,c)]
            if r == 0:
                return 1
            if c == 0:
                return 1
            
            res = dfs(r - 1, c) + dfs(r ,c - 1)
            cache[(r,c)] = res
            return res

        return dfs(m - 1, n- 1)