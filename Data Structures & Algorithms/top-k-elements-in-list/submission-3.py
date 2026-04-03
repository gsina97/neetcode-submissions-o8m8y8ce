class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)

        
        maxHeap = []
        for key,val in c.items():
            maxHeap.append((- val,key))
        
        heapq.heapify(maxHeap)

        res = []
        for i in range(k):
            val, key = heapq.heappop(maxHeap)
            res.append(key)
        
        return res
