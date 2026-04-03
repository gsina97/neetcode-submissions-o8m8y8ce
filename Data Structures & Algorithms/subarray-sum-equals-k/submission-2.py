class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        curr = 0
        cache = {0:1}

        for n in nums:

            curr += n

            if curr - k in cache:
                res += cache[curr - k]
            
            cache[curr] = cache.get(curr, 0) + 1
        return res

