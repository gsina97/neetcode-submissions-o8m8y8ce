class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        l = 1
        r = max(piles)
        res = len(piles)
        while r >= l:
            m = (l + r)//2

            
            total_h = 0
            for i in range(len(piles)):
                total_h += math.ceil(piles[i]/m)
            
            # if valid, 
            if total_h <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
                

        return res