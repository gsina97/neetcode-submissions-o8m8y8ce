class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while r >= l:
            m = (r + l) // 2

            total = 0
            for p in piles:
                total += math.ceil(p/m)
            if total <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res