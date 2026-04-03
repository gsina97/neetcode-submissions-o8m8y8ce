class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)

        heap = []
        for item, cnt in c.items():
            heapq.heappush(heap, (-cnt, item))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res