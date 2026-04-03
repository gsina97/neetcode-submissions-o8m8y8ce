class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and nums[i - 1] == val:
                continue
            
            l, r = i + 1, len(nums) -1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]

                if sum3 == 0:
                    res.append([val , nums[l] , nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                elif sum3 > 0:
                    r -= 1
                else:
                    l += 1
        return res