class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        res = 0
        for n in nums:
            if n - 1 in s:
                continue
            
            lon = 0
            while n + lon in s:
                lon += 1
                res = max(lon, res)
        
        return res