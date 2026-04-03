class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        def findPath(i,j):
            # if i < 0 or j < 0 or i == m or j == m:
            #     return 0
            if i == 0 or j == 0:
                return 1


            left = findPath(i,j - 1)
            up = findPath(i - 1, j)
            return up + left
        
        return findPath(m - 1,n - 1)