class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l = 0
        r = len(nums) - 1

        while r > l:
            m = (l + r) // 2

            val = nums[m]

            if nums[r] < val:
                l = m + 1
            else:
                r = m
        
        min_val = nums[r]
        if r == 0:
            l = 0
            r = len(nums) - 1
        elif nums[0] <= target <= nums[r - 1]:
            l = 0
            r = r - 1
        else:
            l = r
            r = len(nums) - 1
        
        while r >= l :
            m = (r + l) // 2
            val = nums[m]

            if val == target:
                return m
            elif val > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1
