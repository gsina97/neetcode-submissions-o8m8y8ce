class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        l = 1
        r = max(piles)
        res = max(piles)

        while r >= l:
            m = (l + r) // 2

            tmp = 0
            for i in range(len(piles)):
                tmp += math.ceil(piles[i]/m)
            if tmp > h:
                l = m + 1
            else:
                res = min(res, m)
                r = m - 1
        return res

