class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        hs = defaultdict(list)

        for s in strs:
            tmp = [0] * 26
            for c in s:
                tmp[ord(c) - ord('a')] += 1
            
            hs[tuple(tmp)].append(s)
        
        res = []

        for k, val in hs.items():
            res.append(val)
        
        return res