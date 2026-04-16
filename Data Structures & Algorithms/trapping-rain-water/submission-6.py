class Solution:
    def trap(self, height: List[int]) -> int:

        currMaxL = 0
        maxL = [0] * len(height)

        for i in range(len(height)):
            maxL[i] = currMaxL
            currMaxL = max(currMaxL, height[i])

        currMaxR = 0
        maxR = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            maxR[i] = currMaxR
            currMaxR = max(currMaxR, height[i])

        res = 0
        for i in range(len(height)):
            tmp =  max(0, min(maxR[i], maxL[i]) -  height[i])
            if tmp:
                print(tmp)
            res += tmp

        print(maxL)
        print(maxR)

        return res
