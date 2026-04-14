class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        hs = set()


        res = 0

        l = 0
        for i in range(len(s)):
            while s[i] in hs:
                hs.remove(s[l])
                l += 1
            
            hs.add(s[i])
            res = max(res, i - l + 1)
        return res

