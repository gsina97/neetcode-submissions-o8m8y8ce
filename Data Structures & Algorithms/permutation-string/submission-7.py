class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0

        s1Counter = Counter(s1)
        s2Counter = Counter()


        for r in range(len(s2)):
            s2Counter[s2[r]] += 1

            if r - l + 1 > len(s1):
                s2Counter[s2[l]] -= 1
                if s2Counter[s2[l]] == 0:
                    del s2Counter[s2[l]]
                l += 1
            
            if s1Counter == s2Counter:
                return True
        
        return False