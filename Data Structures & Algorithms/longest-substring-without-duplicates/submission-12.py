class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hs = set()
        res = 0
        
        l = 0
        r = 0

        while r < len(s):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            
            hs.add(s[r])
            res = max(res,  r - l + 1)

            r += 1
        return res