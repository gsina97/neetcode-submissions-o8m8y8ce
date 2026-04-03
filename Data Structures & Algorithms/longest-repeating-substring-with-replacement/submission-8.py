class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = {}
        res = 0
        l, r = 0,0

        for r in range(len(s)):

            c[s[r]] = c.get(s[r], 0) + 1
            

            if (r - l + 1) - max(c.values()) > k:
                c[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

