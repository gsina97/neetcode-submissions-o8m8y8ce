class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        
        lside = [0] * n
        maxL = 0
        for i in range(n):
            lside[i] = maxL
            maxL = max(maxL, height[i])

        
        rside = [0] * n
        maxR = 0
        for i in range(n - 1, -1 , -1):
            rside[i] = maxR
            maxR =max(maxR, height[i])

        
        res = 0
        for i in range(n):
            res += max(0, min(lside[i], rside[i])- height[i])
        return res