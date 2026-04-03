class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        def findPaths(i,j):
            if i == 0 or j == 0:
                return 1
            else:

                return findPaths(i,j - 1) + findPaths(i - 1,j )
        
        return findPaths(m - 1, n - 1)