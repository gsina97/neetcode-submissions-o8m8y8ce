class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        water = 0
        while r > l:

            if maxL < maxR:
                l += 1
                temp = maxL - height[l]
                if temp > 0:
                    water += temp
                maxL = max(maxL, height[l])
            else:
                r -= 1
                temp = maxR - height[r]
                if temp > 0:
                    water += temp
                maxR = max(maxR, height[r])
        return water
                 
      