class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap touple -> words


        hashmap = {}

        for word in strs:

            cnts = [0] * 26
            for s in word:
                ord_val = ord("a") - ord(s)
                cnts[ord_val] += 1
            t = tuple(cnts)
            if t not in hashmap:
                hashmap[t] = []
            hashmap[t].append(word)
        
        res = []
        for _, words in hashmap.items():
            res.append(words)
        return res 