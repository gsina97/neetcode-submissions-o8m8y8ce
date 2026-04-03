class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        l = 0
        r = 0
        while r < len(nums):
            nums[l] = nums[r]
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
            k += 1
            l += 1
            r += 1
        return k