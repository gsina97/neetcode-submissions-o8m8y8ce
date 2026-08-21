class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hs = set(nums)

        res = 0
        for n in nums:
            if n - 1 in hs:
                continue
            

            tmp = 0

            while tmp + n in hs:
                tmp += 1
            
            res = max(res, tmp)
        
        return res

        