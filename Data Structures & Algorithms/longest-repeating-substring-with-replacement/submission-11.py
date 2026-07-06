class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hashmap, sliding window (not fixed)
        # 


        hs = Counter()

        l = 0
        res = 0
        for r in range(len(s)):
            hs[s[r]] += 1

            while r - l + 1  - max(hs.values()) > k:
                hs[s[l]] -= 1
                l += 1

            res = max(r - l + 1, res)

        return res
