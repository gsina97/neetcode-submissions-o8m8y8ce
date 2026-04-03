class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        visited = set()

        def bfs(r,c):
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == -1 or (r,c) in visited:
                return

            visited.add((r,c))
            q.append((r,c))
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                bfs(r + 1, c)
                bfs(r , c + 1)
                bfs(r - 1, c)
                bfs(r , c - 1)
                grid[r][c] = dist
            dist += 1
        
        
