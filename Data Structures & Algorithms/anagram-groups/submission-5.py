class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a hashmap, where i can create a list as the key
        hashMap = {}
        
        for s in strs:
            
            key = [0] * 26
            for i in s:
                tmp = ord(i) - ord("a")
                key[tmp] += 1
            if tuple(key) not in hashMap:
                hashMap[tuple(key)] = []
            hashMap[tuple(key)].append(s)
        
        res = []
        for key, valList in hashMap.items():
            res.append(valList)
        
        return res