class Solution:
    def groupAnagrams(self, strs):
        dictionary = {}
        for word in strs:
            sortedWord = tuple(sorted(word))
            if sortedWord not in dictionary:
                dictionary[sortedWord] = []
            dictionary[sortedWord].append(word)
        return list(dictionary.values())