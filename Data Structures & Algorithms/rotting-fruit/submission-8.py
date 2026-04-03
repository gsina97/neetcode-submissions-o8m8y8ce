class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        fresh = 0

        time = 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        def rot(r,c):
            if r == rows or c == cols or r < 0 or c < 0 or grid[r][c] != 1:
                return
            
            grid[r][c] = 2
            q.append((r,c))
            nonlocal fresh
            fresh -= 1

        while q and fresh:
            for i in range(len(q)):
                r,c = q.popleft()
                rot(r + 1,c)
                rot(r,c + 1)
                rot(r - 1,c)
                rot(r,c - 1)
            time +=1
        
        return time if not fresh else -1
                