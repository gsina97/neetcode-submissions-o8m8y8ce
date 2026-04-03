class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while r > l:
            
            width = r - l
            h = min(heights[l], heights[r])
            res = max(res, h * width)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return res
