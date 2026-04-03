class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])


        def dfs(row, col):
            if row == ROWS or col == COLS or row < 0 or col < 0 or grid[row][col] != 1:
                return 0

            grid[row][col] = 0
            return 1 + dfs(row - 1 , col)  + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))
        
        return res
