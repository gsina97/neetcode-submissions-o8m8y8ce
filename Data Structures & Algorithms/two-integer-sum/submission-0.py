class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in map1:
                return [map1[diff], index]
            map1[value] = index