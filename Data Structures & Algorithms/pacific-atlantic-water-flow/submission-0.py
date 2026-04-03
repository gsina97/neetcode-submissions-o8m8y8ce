class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows , cols = len(heights), len(heights[0])

        pacSet , atlSet = set(), set()


        def dfs(r, c, visitSet, prevHeight):
            if (r,c) in visitSet or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight:
                return

            visitSet.add((r,c))
            dfs(r + 1, c, visitSet, heights[r][c])
            dfs(r , c + 1, visitSet, heights[r][c])
            dfs(r - 1, c, visitSet, heights[r][c])
            dfs(r , c - 1, visitSet, heights[r][c])
            
            

        for c in range(cols):
            dfs(0, c, pacSet, heights[0][c])

            dfs(rows - 1, c, atlSet, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacSet, heights[r][0])

            dfs(r, cols - 1, atlSet, heights[r][cols - 1])


        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacSet and (r,c) in atlSet:
                    result.append([r,c])

        return result
