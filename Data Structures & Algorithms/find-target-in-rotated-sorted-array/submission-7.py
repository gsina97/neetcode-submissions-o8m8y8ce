class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first find deflection point.
        # then 3 cases, search left, search right, or array is correctly sorted, so earch all

        l, r = 0, len(nums) - 1

        while r >= l:
            m = (l + r) // 2

            val = nums[m]

            if nums[r] > val:
                r = m
            else:
                l = m + 1

        min_p = r

        if min_p == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[min_p] and target <= nums[-1]:
            l, r = min_p, len(nums) - 1
        else:
            l, r = 0, min_p

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