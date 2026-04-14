class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hs = {}

        for i in range(len(nums)):
            if target - nums[i] in hs:
                return [hs[ target - nums[i]], i]
            hs[nums[i]] = i