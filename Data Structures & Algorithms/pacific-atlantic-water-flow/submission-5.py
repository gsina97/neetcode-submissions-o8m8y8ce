class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        visitedP = set()
        visitedA = set()
        def explore(r,c, s, prev):
            if r == rows or c == cols or r < 0 or c < 0 or (r,c) in s or heights[r][c] < prev:
                return
            

            s.add((r,c))
            explore(r + 1, c, s, heights[r][c])
            explore(r - 1, c, s, heights[r][c])
            explore(r, c + 1, s, heights[r][c])
            explore(r, c - 1, s, heights[r][c])
            return
        

        for r in range(rows):
            # pacific
            explore(r, 0, visitedP, float("-inf"))
            # atlantic
            explore(r, cols - 1, visitedA, float("-inf"))


        for c in range(cols):
            # pacific
            explore(0, c, visitedP, float("-inf"))
            # atlantic
            explore(rows - 1, c, visitedA, float("-inf"))


        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in visitedA and (r,c) in visitedP:
                    res.append([r,c])
        return res
        