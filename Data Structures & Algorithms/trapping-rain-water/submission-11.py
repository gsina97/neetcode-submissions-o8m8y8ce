class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        n = len(height)
        lside = [0] * n
        lmax = 0
        for i in range(n):
            lside[i] = lmax
            lmax = max(lmax, height[i])


        rside = [0] * n
        rmax = 0
        for i in range(n - 1, -1, - 1):
            rside[i] = rmax
            rmax = max(rmax, height[i])

        res = 0
        for i in range(n):
            res += max(0,  min(lside[i], rside[i]) - height[i] )
        
        return res
            