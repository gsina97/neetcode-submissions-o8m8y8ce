class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx, val in enumerate(nums):
            if idx > 0 and nums[idx - 1] == val:
                continue

            l = idx + 1
            r = len(nums) - 1

            while l < r:
                
                s = nums[idx] + nums[l] + nums[r]


                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else: # s = 0
                    res.append([nums[idx] ,nums[l] , nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1

             
            
        return res