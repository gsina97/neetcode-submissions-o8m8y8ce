class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1
        l = 0
        hashSet = set()

        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            
            hashSet.add(s[r])

            res = max(len(hashSet), res)
        
        return res if s else 0
            


        