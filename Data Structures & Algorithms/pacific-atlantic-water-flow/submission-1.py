class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows , cols = len(heights), len(heights[0])

        pacSet, atlSet = set(), set()


        def dfs(r, c, visited, prevHeight):
            if r == rows or c == cols or r < 0 or c < 0 or prevHeight > heights[r][c] or (r,c) in visited:
                return

            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r , c + 1 , visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r , c - 1, visited, heights[r][c])


        # first row
        # last row
        for c in range(cols):
            dfs(0, c, pacSet, heights[0][c])

            dfs(rows -1 , c, atlSet, heights[rows - 1][c])
        
        # left and right side
        for r in range(rows):
            dfs(r, 0, pacSet, heights[r][0])

            dfs(r, cols - 1, atlSet, heights[r][cols - 1])
        

        output = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacSet and (r,c) in atlSet:
                    output.append([r,c])

        return output

        
        

