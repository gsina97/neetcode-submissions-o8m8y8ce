class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}

        for i in range(len(numbers)):
            if target - numbers[i] in hashset:
                return [hashset[target - numbers[i]] + 1, i + 1]
            hashset[numbers[i]] = i
