class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        out = 0

        while r > l:
            x = r - l
            y = min(heights[l], heights[r])
            res = x * y
            out = max(out, res)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return out