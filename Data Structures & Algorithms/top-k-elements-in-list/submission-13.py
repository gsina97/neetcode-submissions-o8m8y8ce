class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        c = Counter(nums)
        
        heap = []
        for num, cnt in c.items():
            heapq.heappush(heap, [-cnt, num])
        res = []

        for i in range(k):
            if heap:
                res.append(heapq.heappop(heap)[1])
        
        return res