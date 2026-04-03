class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dedup = set()
        maxLength = 0
        l = 0

        for r in range(len(s)):
            while s[r] in dedup:
                dedup.remove(s[l])
                l += 1
            dedup.add(s[r])
            maxLength = max(maxLength, len(dedup))
        return maxLength
        