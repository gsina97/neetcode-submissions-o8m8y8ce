class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        dist = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
                    
        directions = [[0,1], [1, 0], [0, -1], [-1, 0]]

        def bfs(r,c):
            if r == rows or c == cols or c < 0 or r < 0 or (r,c) in visited or grid[r][c] == -1:
                return
            
            
            visited.add((r,c))
            q.append((r,c))


        while q:
            for i in range(len(q)):
                r ,c = q.popleft()
                for nr, nc in directions:
                    grid[r][c] = dist
                    bfs(nr + r, nc + c)
            dist += 1
