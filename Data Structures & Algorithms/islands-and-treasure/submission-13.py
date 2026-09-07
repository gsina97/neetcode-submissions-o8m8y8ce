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

        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        dist = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                visited.add((r,c))
                grid[r][c] = dist

                for dr, dc in directions:
                    newR, newC = dr + r , dc + c

                    if newR < 0 or newC < 0 or newC == cols or newR == rows or (newR, newC) in visited or grid[newR][newC] == -1:
                        continue
                    q.append((newR, newC))
                    visited.add((newR, newC))
            dist += 1
        
        

                    

