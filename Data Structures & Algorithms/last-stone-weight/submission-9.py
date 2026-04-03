class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            s1 = abs(heapq.heappop(heap))
            s2 = abs(heapq.heappop(heap))

            res = abs(s1 - s2)
            if res > 0:
                heapq.heappush(heap, - res)
        
        return -heap[0] if heap else 0

