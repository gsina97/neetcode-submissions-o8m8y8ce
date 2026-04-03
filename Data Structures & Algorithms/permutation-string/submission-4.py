class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        l = 0
        windowCounter = Counter()
        s1Counter = Counter(s1)

        for r in range(len(s2)):
            windowCounter[s2[r]] += 1

            # invalid window
            if r - l + 1 > k:
                windowCounter[s2[l]] -= 1
                if windowCounter[s2[l]] == 0:
                    del windowCounter[s2[l]]
                l += 1

            if windowCounter == s1Counter:
                return True
        
        return False
