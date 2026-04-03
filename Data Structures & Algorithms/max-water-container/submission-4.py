class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0

        l, r = 0, len(heights) - 1

        while r > l:
            
            y = min(heights[r], heights[l])
            x = r - l
            h = y * x
            maxArea = max(maxArea, y * x)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxArea 