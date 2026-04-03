class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mapping = {}
        def find(i, j):
            if (i,j) in mapping:
                return mapping[(i,j)]
            elif i == len(text1) or j == len(text2):
                return 0
            elif text1[i] == text2[j]:
                res = 1 + find(i + 1, j + 1)
                mapping[(i,j)] = res
                return res
            else:
                res = max(find(i + 1, j), find(i, j+1))
                mapping[(i,j)] = res
                return res

        return find(0,0)