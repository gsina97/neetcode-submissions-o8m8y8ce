class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        result = 0

        rows, cols = len(grid), len(grid[0])

        

        def dfs(i ,j, currSize):
            if i >= rows or j >= cols or i < 0 or j < 0 or grid[i][j] == 0:
                print("base")
                return 0


            grid[i][j] = 0
            currSize += 1
            print("im in")

            return 1 + dfs(i + 1, j, currSize) + dfs(i - 1, j, currSize) + dfs(i, j + 1, currSize) +dfs(i, j - 1, currSize)
            
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    size = dfs(i,j, 0)
                    result = max(result, size)

        return result