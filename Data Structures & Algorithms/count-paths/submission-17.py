class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        cache = {}
        def dfs(i, j):
            if i == 0 or j == 0:
                return 1
            if (i,j) in cache:
                return cache[(i,j)]
            

            tmp = dfs(i - 1, j) + dfs(i, j - 1)
            cache[(i,j)] = tmp

            return tmp

        
        return dfs(m - 1, n - 1)