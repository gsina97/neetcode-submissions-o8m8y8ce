class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # use a map val -> idx
        counter = {}

        for idx, val in enumerate(nums):
            if target - val in counter:
                return [counter[target - val], idx]
            counter[val] = idx
        