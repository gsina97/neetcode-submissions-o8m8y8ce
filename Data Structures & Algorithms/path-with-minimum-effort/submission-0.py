class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        adj = defaultdict(list)
        rows = len(heights)
        cols = len(heights[0])
        visited = set()




        heap = []
        heapq.heappush(heap, [0,0,0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]


        while heap:
            d, x, y = heapq.heappop(heap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            if (x,y) == (rows - 1, cols - 1):
                return d

            for dr, dc in directions:
                newR, newC = dr + x, dc + y

                if newR < 0 or newC < 0 or newR == rows or newC == cols or (newR,newC) in visited:
                    continue
                diff = max(d, abs(heights[x][y] - heights[newR][newC]))
                heapq.heappush(heap, [diff, newR, newC])
