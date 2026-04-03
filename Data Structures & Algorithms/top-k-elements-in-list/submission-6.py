class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []

        hashMap = Counter(nums)

        for key, cnt in hashMap.items():
            heapq.heappush(heap, (cnt, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res