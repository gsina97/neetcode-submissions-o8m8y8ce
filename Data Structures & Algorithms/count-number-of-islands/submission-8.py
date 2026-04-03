class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if r == rows or c == cols or r < 0 or c < 0 or grid[r][c] != "1":
                return 
            
            grid[r][c] = "0"
            
            dfs(r + 1,c)
            dfs(r ,c+ 1)
            dfs(r - 1,c)
            dfs(r,c - 1)
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r,c)
        return res