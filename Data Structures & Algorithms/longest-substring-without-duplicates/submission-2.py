class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dedup = set()
        l = 0
        maxLen = 0

        for r in range(len(s)):
            while s[r] in dedup:
                dedup.remove(s[l])
                l += 1
            dedup.add(s[r])
            maxLen = max(maxLen, r - l + 1)

        return maxLen
            
