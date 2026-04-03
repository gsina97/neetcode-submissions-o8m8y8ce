class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1


        while r >= l:
            m = (r + l) // 2

            val = nums[m]

            if val > target:
                r = m - 1
            elif val < target:
                l = m + 1
            else:
                return m
        
        return -1