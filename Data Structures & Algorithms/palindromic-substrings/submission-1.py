class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0

        totalLen = len(s)

        for i in range(totalLen):
            
            l,r = i,i
            while l >= 0 and r < totalLen and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1


            l,r = i,i + 1
            while l >= 0 and r < totalLen and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1
        return total