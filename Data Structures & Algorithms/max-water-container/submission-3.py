class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = 0

        l, r = 0, len(heights) - 1

        while r > l:
            h = min(heights[l], heights[r])
            w = r - l 
            total = h * w
            maxHeight = max(maxHeight, total)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxHeight