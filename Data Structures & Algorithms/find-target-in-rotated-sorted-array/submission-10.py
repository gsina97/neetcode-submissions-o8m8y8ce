class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while r > l:

            m = (l + r) // 2

            val = nums[m]
            if val > nums[r]:
                l = m + 1
            else:
                r = m
        
        min_i = r

        if nums[0] <= nums[-1]:
            l = 0
            r = len(nums) -1
        elif target >= nums[min_i] and target <= nums[-1]:
            l = min_i
            r = len(nums) - 1
        else:
            l = 0
            r = min_i - 1
        
        while r >= l:
            m = (l + r) // 2

            val = nums[m]
            if val == target:
                return m
            elif target > val:
                l = m + 1
            else:
                r = m - 1
        
        return -1
