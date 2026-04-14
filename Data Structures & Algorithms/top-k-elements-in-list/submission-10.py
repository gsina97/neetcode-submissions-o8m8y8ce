class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        c = Counter(nums)

        h = []
        for num, cnt in c.items():
            heapq.heappush(h, (-cnt, num))

        
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res