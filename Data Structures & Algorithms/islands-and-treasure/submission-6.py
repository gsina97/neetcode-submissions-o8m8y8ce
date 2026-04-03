class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # call dfs from chests
        # if its a 0, stop
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        def explore(r,c):
            if r == rows or c == cols or c < 0 or r < 0 or (r,c) in visited or grid[r][c] == -1:
                return
            
            q.append((r,c))
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        distance = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance
                explore(r +1,c)
                explore(r,c +1)
                explore(r -1,c)
                explore(r,c -1)
            distance +=1
