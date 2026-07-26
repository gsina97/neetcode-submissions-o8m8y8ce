class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        c1 = Counter(s1)

        c2 = Counter()
        
        r = 0
        l = 0

        while r < len(s2):
            c2[s2[r]] += 1

            if r - l + 1 > len(s1):
                c2[s2[l]] -= 1
                if c2[s2[l]] == 0:
                    del c2[s2[l]]
                l += 1
            
            if c2 == c1:
                return True
            r += 1
        return False



    # hidsaiod
    # hi


   