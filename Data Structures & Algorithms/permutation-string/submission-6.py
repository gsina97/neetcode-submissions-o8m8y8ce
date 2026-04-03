class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapS1 = Counter(s1)
        mapWindow = Counter()
        l = 0

        for r in range(len(s2)):
            mapWindow[s2[r]] += 1


            
            if r - l + 1 > len(s1):
                mapWindow[s2[l]] -= 1
                if mapWindow[s2[l]] == 0:
                    del mapWindow[s2[l]]
                l += 1
            if mapWindow == mapS1:
                return True
        
        return False