class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        res = max(piles)

        l = 1
        r = res

        while r >= l:
            m = (l + r) // 2

            tmp = 0
            for p in piles:
                tmp += math.ceil(p/m)
            if tmp <= h:
                res = min(res, m)
                r = m -1
            else:
                l = m + 1
        return res