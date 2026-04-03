class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        idx = 0
        for idx in range(len(nums)):
            if idx != 0 and nums[idx] == nums[idx - 1]:
                continue


            l = idx + 1
            r = len(nums) - 1

            while r > l:
                s = nums[idx] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[idx],nums[l] ,nums[r]])
                    l += 1
                    r -= 1
                    while r > l and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
        return res

            