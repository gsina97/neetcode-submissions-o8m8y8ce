class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            # alwayus push on heap

            # when to start recording:
            # if window is 1, 0 > 1
            if i + 1 >= k:
                # now that we record, need to delete old records, not in window anymore
                # if element is idx4 , and window is 
                # 
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res