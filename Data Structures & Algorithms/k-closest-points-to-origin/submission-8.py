class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        # (dist, x, y)
        for x, y in points:
            heapq.heappush(heap, (x ** 2  + y  ** 2, x, y))

        res = []
        for i in range(k):
            element = heapq.heappop(heap)
            res.append([element[1], element[2]])
        return res