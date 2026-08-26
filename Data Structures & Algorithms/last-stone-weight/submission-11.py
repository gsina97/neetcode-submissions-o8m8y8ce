class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for s in stones:
            heapq.heappush(heap, -s)
        

        while len(heap) > 1:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)
            print(s1, s2)
            res = abs(s1 - s2)
            if res > 0:
                heapq.heappush(heap, -res)

        return -heap[0] if heap else 0