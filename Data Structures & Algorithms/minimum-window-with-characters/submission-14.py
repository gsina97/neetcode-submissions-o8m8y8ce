class Solution:
    def minWindow(self, s: str, t: str) -> str:


        countT = Counter(t)
        have = 0
        need = len(countT)
        window = Counter()


        l = 0
        minLen = float("inf")
        res = ""

        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    res = s[l:r + 1]

                window[s[l]] -= 1

                if window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        return res