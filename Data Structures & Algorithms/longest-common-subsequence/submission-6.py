class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mapping = {}
        def findLen(tx1, tx2):
            if (tx1, tx2) in mapping:
                return mapping[(tx1,tx2)]
            print(tx1, tx2)
            if not tx1 or not tx2:
                return 0
            elif tx1[0] == tx2[0]:
                val = findLen(tx1[1:], tx2[1:])
                mapping[(tx1, tx2)] = val + 1
                return 1 + val
            else:
                part1 = findLen(tx1[1:] if len(tx1) > 1 else "", tx2)
                part2 = findLen(tx1, tx2[1:]  if len(tx2) > 1 else "")
                res = max(part1, part2)
                mapping[(tx1, tx2)] = res
                return res
        
        return findLen(text1,text2)


