class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxWater = 0

        while l < r:

            now = min(heights[r], heights[l]) * (r - l)

            maxWater = max(maxWater, now)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1



        return maxWater
