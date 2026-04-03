class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0,0
        
        s1Counter = Counter(s1)
        s2Counter = Counter()
        wordLen = len(s1)

        while r < len(s2):
            s2Counter[s2[r]] += 1

            
            if r - l + 1 > len(s1):
                s2Counter[s2[l]] -= 1
                if s2Counter[s2[l]] == 0:
                    del s2Counter[s2[l]]
                l += 1

            print(s2Counter)
            if s1Counter == s2Counter:
                    return True
            r += 1

        return False
            

        
        
        

        
