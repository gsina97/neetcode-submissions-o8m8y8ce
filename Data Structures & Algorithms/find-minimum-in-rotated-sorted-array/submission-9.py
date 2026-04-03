class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while r > l:
            m = (l + r) // 2

            val = nums[m]

            if val > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[r]