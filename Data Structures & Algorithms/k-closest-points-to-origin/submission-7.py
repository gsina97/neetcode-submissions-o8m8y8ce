class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #  use a heap to store distance. But store a small array like [dist, x, y]. heap stores based on first value/.

        heap = []
        
        for x,y in points:
            heapq.heappush(heap, [x**2 + y ** 2, x , y])
        
        res = []

        while k:
            k -=1
            _, x, y= heapq.heappop(heap)
            res.append([x,y])
        
        return res