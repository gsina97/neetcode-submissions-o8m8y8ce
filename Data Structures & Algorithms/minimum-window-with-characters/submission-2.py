class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        tCounter = Counter(t)
        sCounter = Counter()
        res = ""
        minRes = float("inf")


        for r in range(len(s)):
            sCounter[s[r]] += 1

            while tCounter <= sCounter:
                if r - l + 1 < minRes:
                    res = s[l: r+ 1]
                    minRes = r - l + 1
                sCounter[s[l]] -= 1
                if sCounter[s[l]] == 0:
                    del sCounter[s[l]]
                l += 1
        return res
