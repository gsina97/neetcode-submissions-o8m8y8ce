class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        minLen = len(s)

        sCounter = Counter()
        tCounter = Counter(t)
        l = 0

        for r in range(len(s)):
            sCounter[s[r]] += 1

            while tCounter <= sCounter:
                if r - l + 1 <= minLen:
                    minLen = r - l + 1
                    res = s[l: r + 1]
                sCounter[s[l]] -= 1
                if sCounter[s[l]] == 0:
                    del sCounter[s[l]]
                l += 1
        return res