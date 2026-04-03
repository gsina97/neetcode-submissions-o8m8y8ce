class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        
        q = collections.deque()
        time = 0
        rows , cols = len(grid),  len(grid[0])


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
                    

        directions = [[0,1], [0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row == rows or col == cols or row < 0 or col < 0 or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append((row,col))
                    fresh -= 1
            time += 1
      
        return time if not fresh else -1
            
        
        
