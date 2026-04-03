class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1,2,3   5,6   9,10
        s = set(nums)
        
        res = 0

        for n in nums:
            if n - 1 in s:
                continue
            longest = 0
            while longest + n in s:
                longest += 1
            res = max(res, longest)
        return res