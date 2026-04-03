class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            a = - heapq.heappop(heap)
            b = - heapq.heappop(heap)
            if a > b:
                a -= b
                heapq.heappush(heap, -a)
            elif a < b:
                b -= a
                heapq.heappush(heap, -b)

        return - heap[0] if heap else 0

