class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for idx, n in enumerate(nums):
            if target - n in hashMap:
                return [hashMap[target-n], idx]
            hashMap[n] = idx
            