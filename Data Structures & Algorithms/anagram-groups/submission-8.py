class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        m = defaultdict(list)
        for w in strs:


            l = [0] * 26
            for s in w:
                l[ord(s) - ord('a')] += 1
            
            t = tuple(l)
            m[t].append(w)

        res =[]
        for _, l in m.items():
            res.append(l)
        return res