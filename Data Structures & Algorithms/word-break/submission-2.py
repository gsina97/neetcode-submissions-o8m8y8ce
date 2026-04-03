class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        n = len(s)
        
        for i in range(n):
            if dp[i]:             
                for w in wordDict:
                    if s[i: i + len(w)] == w:
                        dp[len(w) + i] = True
            
        return dp[n]
