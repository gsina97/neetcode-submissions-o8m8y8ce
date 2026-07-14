class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map key = tuple , val = list(str..)

        hs = defaultdict(list)


        for s in strs:

            l = [0] * 26
            for c in s:
                l[ord(c) - ord('a')] += 1
            
            hs[tuple(l)].append(s)

        
        res = []

        for _, val in hs.items():
            res.append(val)
        
        return res

