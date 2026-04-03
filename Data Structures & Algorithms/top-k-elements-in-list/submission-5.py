class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = Counter(nums)
        # num to counter

        heap = []

        for n, cnt in hashMap.items():
            heapq.heappush(heap, (cnt, n))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res
