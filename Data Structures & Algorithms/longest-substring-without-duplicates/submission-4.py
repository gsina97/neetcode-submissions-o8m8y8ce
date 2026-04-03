class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dedup = set()
        output = 0
        l = 0

        for r in range(len(s)):
            while s[r] in dedup:
                dedup.remove(s[l])
                l += 1
            dedup.add(s[r])

            output = max(output, r - l + 1)
        return output

