class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        l = 1
        r = max(piles)
        res = max(piles)

        while r >= l:
            m = (l + r) // 2

            # m = banana each times times
            total_h = 0
            for bananas in piles:
                total_h += math.ceil(bananas/m)
            
            if total_h > h:
                l = m + 1
            else:
                res = min(m, res)
                r = m - 1

        return res