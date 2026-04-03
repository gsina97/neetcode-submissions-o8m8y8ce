class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l  = 0 
        r = len(nums) - 1

        while r > l:
            m = (l + r) // 2

            val = nums[m]

            if val > nums[r]: 
                l = m + 1
            else:
                r = m
        min_i = r

        if min_i == 0:
            # print("xxxxxx")

            l = 0
            r = len(nums) - 1
        elif nums[min_i] <= target <= nums[-1]:
            print("xxxxxx")

            l = min_i
            r = len(nums) -1
        else:
            l = 0
            r = min_i
        
        print(l, r)
        while r >= l:
            m = (l + r) // 2

            val = nums[m]
            if val == target:
                return m
            elif val > target:
                r = m - 1
            else:
                l = m + 1

        return -1
