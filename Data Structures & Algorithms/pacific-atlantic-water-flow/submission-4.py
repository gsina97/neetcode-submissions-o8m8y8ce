class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        


        # find what pacific water touch
        # find what atlantic water touches
        # find union


        # find pacific

        visitedP = set()
        visitedA = set()

        rows = len(heights)
        cols = len(heights[0])
        def dfs(r,c, w, s):
            if r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < w or (r,c) in s:
                return
            
            s.add((r,c))
            dfs(r + 1, c, heights[r][c], s)
            dfs(r - 1, c, heights[r][c], s)
            dfs(r , c+ 1, heights[r][c], s)
            dfs(r , c - 1, heights[r][c], s)

        for i in range(rows):
            # pacific left edge
            dfs(i, 0, 0,  visitedP)
            # atlantic - top side
            dfs(i, cols - 1, 0, visitedA)

        for i in range(cols):
            # pacific
            dfs(0, i, 0, visitedP)
            # atlantic
            dfs(rows - 1, i, 0, visitedA)

        

        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in visitedA and (r,c) in visitedP:
                    res.append([r,c])

        return res



        