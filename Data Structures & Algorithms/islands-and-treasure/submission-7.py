class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        q = deque()

        def explore(r,c):
            if r == rows or c == cols or r < 0 or c < 0 or (r,c) in visited or grid[r][c] == -1:
                return
            
            visited.add((r,c))
            q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                explore(r-1, c)
                explore(r+1, c)
                explore(r, c-1)
                explore(r, c+1)
            dist += 1

