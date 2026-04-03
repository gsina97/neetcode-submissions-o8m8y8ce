class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hashmap ->  value -> idx

        hashMap = {}

        for i in range(len(numbers)):
            if target - numbers[i] in hashMap:
                return [1+ hashMap[target - numbers[i]], 1 + i]

            hashMap[numbers[i]] = i
        