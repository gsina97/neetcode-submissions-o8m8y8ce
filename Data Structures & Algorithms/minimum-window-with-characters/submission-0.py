class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowMap = Counter()
        mapT = Counter(t)
        l = 0
        minSize = float("inf")
        res = ""


        for r in range(len(s)):
            windowMap[s[r]] += 1

            while mapT <= windowMap:
                windowLen = r - l + 1
                if windowLen < minSize:
                    minSize = windowLen
                    res = s[l:r+1]
                
                windowMap[s[l]] -= 1
                if windowMap[s[l]] == 0:
                    del windowMap[s[l]]
                l += 1
        return res
