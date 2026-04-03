class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        res = 0
        currSum = 0

        mapping = {0: 1}

        for n in nums:
            currSum += n

            if (currSum - k ) in mapping:
                res += mapping.get(currSum - k, 0) 
            mapping[currSum] = mapping.get(currSum, 0) + 1
            
        
        return res