class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a second arr, sort it.
        # create a map key is sorted number-> list


        cache = {} # tuple ([counter for each letter, 0,0,01,0,1 x26]) -> value [da,ad..]

        for i in range(len(strs)):

            tmp = [0] * 26
            for j in range(len(strs[i])):
                tmp[ord("a")- ord(strs[i][j])] += 1
            
            t = tuple(tmp)
            if t not in cache:
                cache[t] = []
            cache[t].append(strs[i])
        

        res = []

        for _, l in cache.items():
            res.append(l)
        
        return res
            