class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        hs = Counter()
        res = 0
        for r in range(len(s)):
            hs[s[r]] += 1            

        # len of window - maxValue -> how many other letters
            while r - l + 1 -  max(hs.values()) > k:
               hs[s[l]] -= 1
               l += 1

            res = max(res, r - l + 1)

        return res 