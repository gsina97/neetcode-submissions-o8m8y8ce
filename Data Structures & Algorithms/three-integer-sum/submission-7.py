class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx,val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            

            l = idx + 1
            r = len(nums) - 1
            while l < r:
                s = nums[l] + nums[r] + val

                if s == 0:
                    res.append([nums[l], nums[r], val])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res