class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.res = 0
        self.cache = {}

        def find(i,j):
            if (i,j) in self.cache:
                return self.cache[(i,j)]
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                self.cache[(i,j)] = 1 + find(i + 1, j + 1)
                return self.cache[(i,j)]
            else:
                res = max(find(i + 1, j), find(i, j + 1))
                self.cache[(i,j)] = res
                return res
        
        return find(0,0)