class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            newWord = str(len(s)) + "#" + s
            res.append(newWord)
        # print("".join(res))
        return "".join(res)

    def decode(self, s: str) -> List[str]:

        res = []
        r = 0

        while r < len(s):

            i = r

            while s[i] != "#":
                i += 1
            
            length = int(s[r: i])
            # print = length()
            word = s[i + 1: i + 1 + length]
            res.append(word)

            r = i + 1 + length
        
        return res

