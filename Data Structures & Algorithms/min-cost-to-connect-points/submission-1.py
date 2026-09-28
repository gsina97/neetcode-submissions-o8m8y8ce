class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        heap = []


        # cost, idx
        heapq.heappush(heap, (0,0))

        
        visited = set()
        total = 0
        while heap:
            cost, idx = heapq.heappop(heap)
            if idx in visited:
                continue
            visited.add(idx)
            total += cost

            for i in range(len(points)):
                if i in visited:
                    continue
                heapq.heappush(heap, (abs(points[i][0] - points[idx][0]) + abs(points[i][1] - points[idx][1]), i) )

        return total