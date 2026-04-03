class Solution:
# get each word length, on the string append len + # + word

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            res.append(str(len(word)) + "#" + word)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:

        res = []

        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i: j ])
            word = s[j + 1: j + length + 1]
            res.append(word)
            i = j + 1 + length
            
        return res
