class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # use a heap
        #  add all elements O(n)
        # pop k times. kth pop is my return value

        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
            
        
        return heap[0]