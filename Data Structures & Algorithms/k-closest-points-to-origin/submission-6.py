class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        # x + y

        # (x+y), (x,y)

        for x,y in points:
            heapq.heappush(heap, (x ** 2 + y**2,x,y))
        
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
        
        return res