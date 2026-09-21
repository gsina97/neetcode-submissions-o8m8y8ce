class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hs = {}


        for i in range(len(numbers)):
            if target - numbers[i] in hs:
                return [1 + hs[target - numbers[i]], i + 1]
            
            hs[numbers[i]] = i
        