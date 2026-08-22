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
            

        res = 0
        for i in range(len(height)):
            res += max(min(lside[i], rside[i]) - height[i], 0)
        
        return res
            

        