class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        res = 0
        for n in nums:
            if n - 1 not in s:

                longest = 0
                while longest + n in s:
                    longest += 1
                    
                res = max(res, longest)
        
        return res