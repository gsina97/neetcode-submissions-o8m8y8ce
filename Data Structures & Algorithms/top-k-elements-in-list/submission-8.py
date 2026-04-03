class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        c = Counter(nums)

        heap = []

        for key, cnt in c.items():
            heapq.heappush(heap, (-cnt, key))

        
        res = []

        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1


        return res