class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        out = 0
        while r > l:
            res = min(heights[r] , heights[l]) * (r - l)

            out = max(out, res)
            
            if heights[r] > heights[l]:
                l +=1
            elif heights[r] < heights[l]:
                r -=1
            else:
                r-=1
                l+=1
        return out