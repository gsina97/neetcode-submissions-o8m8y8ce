class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        res = 0
        print(nums)
        for i in range(len(nums) - k):
            res = heapq.heappop(nums)
            print("popping: ", res)

        
        return nums[0]