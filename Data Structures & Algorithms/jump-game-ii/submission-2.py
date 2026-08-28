class Solution:
    def jump(self, nums: List[int]) -> int:
        

        res = 0
        l  = r = 0
        n = len(nums)


        while r < n - 1:
            farthest = r
            
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            res += 1
            l = r + 1
            r = farthest
        
        return res
