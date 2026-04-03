class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        total = 0

        directions = [[0,1] , [0, -1], [1,0], [-1, 0]]



        def dfs(r, c):
            if r == rows or c == cols or r < 0 or c < 0 or grid[r][c] == "0":
                return


            grid[r][c] = "0"
            
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    total +=1 
                    dfs(r,c)

        return total
        









        

