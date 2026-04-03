class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        counter = Counter(nums)

        heap = []
        for val, cnt in counter.items():
            heapq.heappush(heap, (- cnt, val))

        res = []
        while k:
            k -=1
            res.append(heapq.heappop(heap)[1])
        
        return res

