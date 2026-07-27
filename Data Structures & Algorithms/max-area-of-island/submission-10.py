class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])



        visited = set()
        def bfs(i,j):
            if i < 0 or i == rows or j < 0 or j == cols or (i,j) in visited or grid[i][j] != 1:
                return 0
            
            visited.add((i,j))
            res = bfs(i + 1, j) + bfs(i - 1, j) + bfs(i , j+ 1) + bfs(i , j - 1)

            return res + 1
        
        for i in range(rows):
            for j in range(cols):
                res = max(res, bfs(i,j))

        return res