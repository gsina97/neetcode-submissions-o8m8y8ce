class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # check if t is subset of s
        res = s + "x"
        
        ct = Counter(t)
        cs = Counter()
        l = 0
        for r in range(len(s)):
            cs[s[r]] += 1

            while ct <= cs:
                if r - l + 1 < len(res):
                    res = s[l:r + 1]
                cs[s[l]] -= 1
                if not cs[s[l]]:
                    del cs[s[l]]
                l += 1
        
        return res if len(res) <= len(s) else ""