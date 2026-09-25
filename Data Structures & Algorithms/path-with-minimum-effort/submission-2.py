class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])



        heap = [[0,0,0]]

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        while heap:
            dist, r, c = heapq.heappop(heap)
            if (r,c) == (rows - 1, cols - 1):
                return dist
            if (r,c) in visited:
                continue
            visited.add((r,c))
            
            for dr, dc in directions:
                newr, newc = dr + r , dc + c

                if newr == rows or newc == cols or newr < 0 or newc < 0:
                    continue
                
                heapq.heappush(heap, [max(abs(heights[r][c] - heights[newr][newc]), dist), newr, newc])
        
                
            
