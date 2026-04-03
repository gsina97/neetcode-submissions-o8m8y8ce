class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapping = {0: 1}

        curr = 0

        res = 0
        for n in nums:
            curr += n

            if (curr - k) in mapping:
                res += mapping[curr-k]
            
            mapping[curr] = mapping.get(curr, 0) + 1
        return res 