class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        visited = set()

        heap = []
        # cost, idx
        heapq.heappush(heap, (0, 0))

        total = 0
        while heap:
            cost, idx = heapq.heappop(heap)
            if idx in visited:
                continue
            visited.add(idx)
            total += cost

            for i in range(len(points)):
                if i not in visited:
                    heapq.heappush(heap, (abs(points[idx][0] - points[i][0]) + abs(points[idx][1] - points[i][1]) ,i))
        
        return total