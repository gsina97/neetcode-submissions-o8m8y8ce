class Solution:
    # 43$$word
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            l = len(s)
            res.append(str(l) + "#" + s)
        return "".join(res) 


# 
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):

            r = i

            while s[r] != "#":
                r += 1
            #     3#lol4#helo
            #       ^      
            length = int(s[i:r])
            word = s[r + 1: r + length + 1]
            res.append(word)
            i = r + length + 1
        return res
