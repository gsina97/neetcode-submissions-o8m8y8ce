class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        time = 0

        q = collections.deque()

        def addRot(r,c):
            if r == rows or c == cols or r < 0 or c < 0 or grid[r][c] != 1:
                return
            nonlocal fresh
            grid[r][c] = 2
            fresh -= 1
            q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                addRot(r + 1,c)
                addRot(r,c + 1)
                addRot(r - 1,c)
                addRot(r,c- 1)
            time += 1
        return time if not fresh else -1