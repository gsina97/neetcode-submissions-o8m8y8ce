class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        l = 0
        r = len(nums) - 1

        while r > l:
            m = (l + r) // 2

            val = nums[m]
            if val > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[r]