class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):

            # if we can take it by itself, if this number isn't 0 ,it can be decoded as a singleton
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]
            
            newNum = int(s[i - 2: i])
            if newNum >= 10 and newNum <= 26:
                dp[i] += dp[i - 2]
        
        return dp[-1]
            