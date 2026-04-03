class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        self.cache = {}
        def find(r,c):
            if (r,c) in self.cache:
                return self.cache[(r,c)]
            if r == 0 or c == 0:
                return 1
            
            left = find(r, c- 1)
            up = find(r - 1, c)
            res = up + left
            self.cache[(r,c)] = res
            return res
        
        return find(m - 1, n - 1)