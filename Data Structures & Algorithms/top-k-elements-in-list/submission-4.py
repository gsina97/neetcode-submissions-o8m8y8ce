class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # max heap, top is max element(idx)

        # number -> count
        mapping = Counter()
        for i, val in enumerate(nums):
            mapping[val] += 1
        
        heap = []
        for key,val in mapping.items():
            heapq.heappush(heap, (- val, key))
        
        res = []
        print(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
