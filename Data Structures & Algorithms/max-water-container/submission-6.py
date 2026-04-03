class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        res = 0

        while r > l:
            
            res = max(res, (r - l) * min(height[l], height[r]))

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res