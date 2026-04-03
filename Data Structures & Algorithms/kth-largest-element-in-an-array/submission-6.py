class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heapq.heappush(heap, - n)

        k -= 1

        while k:
            k -= 1
            heapq.heappop(heap)

        return -heap[0]