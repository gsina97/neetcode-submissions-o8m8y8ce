class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visitedP = set()
        visitedA = set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visited, prevHeight):
            if r == rows or c == cols or r < 0 or c < 0 or (r,c) in visited or heights[r][c] < prevHeight:
                return
            
            visited.add((r,c))
            dfs(r + 1,c, visited, heights[r][c])
            dfs(r,c + 1, visited, heights[r][c])
            dfs(r - 1,c, visited, heights[r][c])
            dfs(r,c - 1, visited, heights[r][c])
        
        for i in range(rows):
            dfs(i, 0, visitedP, heights[i][0])
            dfs(i, cols - 1, visitedA, heights[i][cols - 1])

        for i in range(cols):
            dfs(0, i , visitedP, heights[0][i])
            dfs(rows - 1, i , visitedA, heights[rows-1][i])


        output = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in visitedP and (i,j) in visitedA:
                    output.append([i,j])

        return output


        