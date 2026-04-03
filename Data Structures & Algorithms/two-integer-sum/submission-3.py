class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

# val -> idx
        mapping = {}
        for idx, val in enumerate(nums):
            if target - val in mapping.keys():
                return [mapping[target - val], idx]
            else:
                mapping[val] = idx