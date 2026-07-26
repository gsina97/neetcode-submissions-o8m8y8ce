class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hashmap
        #  value 1 -> idx 0
        # value 2 -> idx 1


        hs = {}

        for i in range(len(numbers)):
            if target - numbers[i] in hs:
                return [hs[target - numbers[i]] + 1, i + 1]
            hs[numbers[i]] = i
        
        