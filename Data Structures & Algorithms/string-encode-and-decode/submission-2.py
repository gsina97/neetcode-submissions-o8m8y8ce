class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for i in range(len(strs)):
            length = len(strs[i])
            out += str(length) + "#" + strs[i]
        return out
      
    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            word = s[j + 1: j + length + 1]
            out.append(word)
            i = j + length + 1
        return out

  
        

