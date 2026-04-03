class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping = {}

        # map val to idx

        for i in range(len(numbers)):
            if target - numbers[i] in mapping:
                return [mapping[target - numbers[i]] + 1, i + 1]
            mapping[numbers[i]] = i
            