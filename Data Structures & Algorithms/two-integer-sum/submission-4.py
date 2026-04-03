class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # val -> idx
        mapping = {}

        for idx, val in enumerate(nums):
            if target - val in mapping:
                return [mapping[target - val], idx]
            mapping[val] = idx
        
