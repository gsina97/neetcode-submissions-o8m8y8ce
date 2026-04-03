class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        def findPath(r, c):
            if r == 0 or c == 0:
                return 1
            if r < 0 or c < 0 or r >= m or c >= n:
                return 0
            
            left = findPath(r, c - 1)
            up = findPath(r - 1, c)
            return up + left
        
        return findPath(m -1 , n - 1)