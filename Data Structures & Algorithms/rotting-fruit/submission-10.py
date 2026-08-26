class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        self.fresh = 0


        q = deque()

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    self.fresh += 1
        
        def rot(r,c):
            if r == rows or c == cols or r < 0 or c < 0 or grid[r][c] != 1 or (r,c) in visited:
                return
            
            self.fresh -= 1
            grid[r][c] = 2
            q.append((r,c))

        time = 0
        while q and self.fresh:
            for i in range(len(q)):
                r,c = q.popleft()
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c - 1)
                rot(r , c+ 1)
            time += 1
        return time if not self.fresh else -1
