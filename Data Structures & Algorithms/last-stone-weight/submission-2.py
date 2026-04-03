class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heapq.heappush(heap, - stones[i])

        while len(heap) > 1:
            x = - heapq.heappop(heap)
            y = - heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, - abs(x - y))
            
        return -heap[0] if heap else 0
        