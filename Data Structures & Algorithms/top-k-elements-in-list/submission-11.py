class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        d = Counter(nums)
        
        for val, cnt in d.items():
            heapq.heappush(heap, (- cnt, val))
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
