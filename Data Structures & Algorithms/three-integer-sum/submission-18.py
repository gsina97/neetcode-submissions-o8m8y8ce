class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []


        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while r > l:
                s = nums[i] + nums[l] + nums[r]

                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                    while r > l and nums[l] == nums[l - 1]:
                        l += 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
            
        return res