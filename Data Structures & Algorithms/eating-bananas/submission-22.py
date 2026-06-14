class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)

        l = 1
        r = max(piles) + 1

        while r >= l:

            m = (l + r) // 2
            tmp = 0
            for i in range(len(piles)):
                tmp += math.ceil(piles[i]/m)
            if tmp <= h:
                res = min(m, res)
                r = m - 1
            else:
                l = m + 1
        
        return res