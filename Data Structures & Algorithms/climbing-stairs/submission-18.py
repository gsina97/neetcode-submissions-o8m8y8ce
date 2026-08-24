class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {0: 1, 1: 1}

        def dfs(n):
            if n == 0:
                return 1
            elif n == 1:
                return 1
            if n in cache:
                return cache[n]
            
            res = dfs(n - 1) + dfs(n - 2)
            cache[n] = res
            return res
        
        return dfs(n)
        