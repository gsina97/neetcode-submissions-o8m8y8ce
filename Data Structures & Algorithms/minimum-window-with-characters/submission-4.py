class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        tC = Counter(t)
        sC = Counter()
        res = ""
        minLen = float("inf")
        
        l = 0
        r = 0
        while r < len(s):
            sC[s[r]] += 1

            while tC <= sC:
                if r - l + 1 <= minLen:
                    minLen = r - l + 1
                    res = s[l:r + 1]
                sC[s[l]] -= 1
                if sC[s[l]] == 0:
                    del sC[s[l]]
                l += 1
            
            r += 1

        return res
