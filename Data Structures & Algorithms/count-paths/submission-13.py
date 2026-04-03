class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        self.cache = {}
        def findPath(i,j):
            if (i,j) in self.cache:
                return self.cache[(i,j)]
            if i == 0 or j == 0:
                return 1
            else:
                left = findPath(i, j - 1)
                up = findPath(i - 1, j)
                res = left + up
                self.cache[(i,j)] = res 
                return res
        
        return findPath(m -1, n - 1)