class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        
        fresh = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))

        def dfs(r,c):
            if r == rows or c == cols or r < 0 or c < 0 or (r,c) in visited or grid[r][c] != 1:
                return

            
            nonlocal fresh
            grid[r][c] = 2
            visited.add((r,c))
            q.append((r,c))
            fresh -= 1
        
        minutes = 0
        while q and fresh:
            for i in range(len(q)):
                r,c = q.popleft()
                dfs(r - 1,c)
                dfs(r ,c- 1)
                dfs(r + 1,c)
                dfs(r ,c + 1)
            minutes += 1
        
        return minutes if not fresh else -1
                