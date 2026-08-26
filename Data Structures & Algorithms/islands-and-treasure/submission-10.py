class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])



        

        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))


        def explore(r,c):
            if r == rows or c == cols or r < 0 or c < 0 or grid[r][c] == -1 or (r,c) in visited:
                return
            
            q.append((r,c))
            visited.add((r,c))
            
        
        curr = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = curr
                explore(r + 1,c)
                explore(r ,c + 1)
                explore(r - 1 ,c )
                explore(r ,c - 1)

            curr += 1
        
