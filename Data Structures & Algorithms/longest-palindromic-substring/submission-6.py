class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        maxlen = 0

        for i in range(len(s)):
            # odd
            l = i
            r = i

            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if r - l + 1 >= maxlen:
                    start = l
                    maxlen = r - l + 1

                l -= 1
                r += 1
            
            l = i
            r = i + 1

            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:

                if r - l + 1 >= maxlen:
                    start = l
                    maxlen = r - l + 1
                l -= 1
                r += 1
        return s[start:start+maxlen]