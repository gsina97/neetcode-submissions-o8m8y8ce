class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        res = max(piles)
        while r >= l:

            m = (r + l) // 2
            
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i]/m)
            if total <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res