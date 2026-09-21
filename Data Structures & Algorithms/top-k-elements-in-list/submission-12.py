class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # top most frequest elements
        # i need somehow to evict the lowest elements, or keep track of the highest ones
        # a heap can do both
        

        heap = []
        c = Counter(nums)



        for num, count in c.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        print(heap)
        res = []
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        return res
