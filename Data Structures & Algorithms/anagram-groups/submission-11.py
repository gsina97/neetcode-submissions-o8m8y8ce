class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        hs = defaultdict(list)

        for word in strs:

            k = [0] * 26
            for i in range(len(word)):
                k[ord(word[i])-ord("a")] += 1
            
            hs[tuple(k)].append(word)
        
        res = []
        
        for l in hs.values():
            res.append(l)

        return res