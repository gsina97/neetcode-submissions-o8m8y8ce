class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dist = 0

        q = collections.deque()


        visited = set()


        rows, cols = len(grid), len(grid[0])

        def addRoom(r,c):
            if r == rows or c == cols or c < 0 or r < 0 or (r,c) in visited or grid[r][c] == -1:
                return
            
            visited.add((r,c))
            q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))



        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r + 1,c)
                addRoom(r, c + 1)
                addRoom(r - 1,c)
                addRoom(r ,c - 1)
            dist += 1
        