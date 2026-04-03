class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowMap = Counter()
        tMap = Counter(t)
        l = 0
        minSize = float("inf")
        res = ""

        for r in range(len(s)):
            windowMap[s[r]] += 1

            while tMap <= windowMap:
                windowMap[s[l]] -= 1
                windowLen = r - l + 1
                if minSize > windowLen:
                    minSize = windowLen
                    res = s[l: r + 1]
                
                l += 1
        return res
