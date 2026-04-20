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
        
        min_idx = r
        print(min_idx)

        l = 0
        r = 0
        if target == nums[min_idx]:
            return min_idx
        elif nums[min_idx] <= target <= nums[-1]:
            l = min_idx
            r = len(nums) - 1
        else:
            l = 0 
            r = min_idx - 1
        
        while r >= l:
            m = (l + r) // 2

            val = nums[m]

            if val > target:
                r = m - 1
            elif val < target:
                l = m + 1
            else:
                return m
        return -1
