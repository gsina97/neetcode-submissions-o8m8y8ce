class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True   # empty prefix is always valid

        for i in range(n):
            if not dp[i]:
                continue   # no valid segmentation up to i, skip
            
            for j in range(i + 1, n + 1):
                if s[i:j] in wordSet:
                    dp[j] = True
        
        return dp[n]
