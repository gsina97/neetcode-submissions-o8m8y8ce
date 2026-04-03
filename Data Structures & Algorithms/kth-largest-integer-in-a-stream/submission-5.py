class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        for i in range(len(nums) - k):
            heapq.heappop(self.heap)
        


        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if self.k < len(self.heap):
            heapq.heappop(self.heap)
        return self.heap[0]
        
