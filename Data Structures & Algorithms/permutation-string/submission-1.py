class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowCounter = Counter()
        s1Counter = Counter(s1)
        l = 0
        k = len(s1)
        
        for r in range(len(s2)):
            windowCounter[s2[r]] += 1

            # if len(window) > k
            if r - l + 1 > k:
                windowCounter[s2[l]] -= 1
                if windowCounter[s2[l]] == 0:
                    del windowCounter[s2[l]]
                l += 1

            if s1Counter == windowCounter:
                return True
        
        return False
            

