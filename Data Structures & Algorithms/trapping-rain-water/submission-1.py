class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)
       

        tempMax = 0
        for i in range(len(height)):
            maxL[i] = tempMax
            tempMax = max(tempMax, height[i])
        
        tempMax = 0
        for i in range(len(height) - 1, -1, -1):
            maxR[i] = tempMax
            tempMax = max(tempMax, height[i])
        
        final = 0
        for i in range(len(height)):
            temp = min(maxL[i], maxR[i]) - height[i]
            if temp > 0:
                final += temp
        
        return final
