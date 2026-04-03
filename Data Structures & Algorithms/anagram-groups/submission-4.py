class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map (touple([a: 0, b: 3, c : 5] -> word))

        mapping = {}
        for word in strs:
            ordering = [0] * 26

            for i in word:
                ordering[ord(i) - ord("a")] += 1
            if tuple(ordering) not in mapping:
                mapping[tuple(ordering)] = []
            mapping[tuple(ordering)].append(word)
        
        res = []
        for key,val in mapping.items():
            res.append(val)

        return res        

