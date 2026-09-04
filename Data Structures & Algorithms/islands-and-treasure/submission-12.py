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

        res = 0

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = res
                visited.add((r,c))
                for dr, dc in directions:
                    newR, newC = dr + r , dc + c
                    
                    if newR < 0 or newR == rows or newC < 0 or newC == cols or (newR, newC) in visited or grid[newR][newC] == -1:
                        continue
                    q.append((newR,newC))
                    visited.add((newR,newC))
            res += 1
        