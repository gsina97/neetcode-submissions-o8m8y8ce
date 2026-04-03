class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        resultMap = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] +=1
            key = tuple(count)
            if key not in resultMap:
                resultMap[key] = []
            resultMap[key].append(word)

        return list(resultMap.values())