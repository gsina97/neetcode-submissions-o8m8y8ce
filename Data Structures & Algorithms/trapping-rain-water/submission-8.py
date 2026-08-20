class Solution:
    def trap(self, height: List[int]) -> int:
        

        maxL = 0
        lside = [0] * len(height)

        for i in range(len(height)):
            lside[i] = maxL
            maxL = max(maxL, height[i])


        maxR = 0
        rside = [0] * len(height)
        for i in range(len(height) - 1, -1 , -1):
            rside[i] = maxR
            maxR = max(maxR, height[i])
        

        totalWater = [0] * len(height)
        for i in range(len(height)):
            totalWater[i] = max(0,min(rside[i], lside[i]) - height[i] )

        # print(totalWater)
        return sum(totalWater)
