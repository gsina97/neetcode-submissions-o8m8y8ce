class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        while r >= l:

            m = (l + r ) // 2
            val = nums[m]
            if val > target:
                r = m - 1
            elif val < target:
                l = m + 1
            else:
                return m
        
        return -1