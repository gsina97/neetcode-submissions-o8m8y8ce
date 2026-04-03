class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find deflection point
        l, r = 0, len(nums) - 1

        while r > l:
            m = (r + l) // 2

            val = nums[m]
            if val > nums[r]:
                l = m + 1
            else:
                r = m
        
        min_i = r

        if min_i == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[min_i] and target <= nums[len(nums)  - 1]:
            l = min_i
            r = len(nums) - 1
        else:
            l, r = 0, min_i - 1
        
        while r >= l:
            m = (r + l) // 2

            val = nums[m]
            if val == target:
                return m
            elif val > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1
