class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        heap = []

        for s in stones:
            heapq.heappush(heap, - s)

        


        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)

            res = abs(a - b)
            if res:
                heapq.heappush(heap, - res)
            
        
        return -heap[0] if heap else 0
