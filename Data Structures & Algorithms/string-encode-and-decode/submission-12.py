class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            # number + hashtag + word
            num = len(s)
            newS = str(num) + "#" + s
            res.append(newS)
        
        return "".join(res)
            
            


    def decode(self, s: str) -> List[str]:
        res = []

        l = 0
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            
            # here r is on hashtag
            wordLen = int(s[l:r])
            newWord = s[r + 1: r + 1 + wordLen]
            res.append(newWord)
            l = r + 1 + wordLen
        
        return res