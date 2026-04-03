class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            l = len(s)
            word = str(l) + "#" + s
            res.append(word)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        
        r = 0
        print(s)
        while r < len(s):
            l = r
            while s[r] != "#":
                r += 1
            
            print(l, r)
            length = int(s[l:r])
            w = s[r + 1: r + 1 + length]
            print(w)
            res.append(w)
            r = r + 1 + length
        return res

