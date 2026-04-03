class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct = Counter(t)

        cs = Counter()
        res = ""
        minLen = float("inf")


        l = 0
        for r in range(len(s)):
            cs[s[r]] += 1

            while ct <= cs:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = s[l:r + 1]
                cs[s[l]] -= 1
                if cs[s[l]] == 0:
                    del cs[s[l]]
                l += 1
            r += 1
        return res