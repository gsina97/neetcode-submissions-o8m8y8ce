class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        
        def find(i,j):
            if i == 0 or j == 0:
                return 1
            
            left = find(i, j - 1)
            up = find(i - 1, j)
            return up + left
        
        return find(m - 1, n - 1)