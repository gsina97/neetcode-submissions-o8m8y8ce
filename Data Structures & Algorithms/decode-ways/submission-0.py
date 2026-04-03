class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp[i] = number of ways to decode substring s[0:i]
        dp = [0] * (n + 1)

        # Base case: empty string has 1 way to decode
        dp[0] = 1

        # First character: if it's '0', no valid decoding
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, n + 1):

            # ----- Single digit decode -----
            # Check if last single digit is valid (1 to 9)
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # ----- Two digit decode -----
            # Check if last two digits form valid letter (10 to 26)
            twoDigit = int(s[i-2:i])
            if 10 <= twoDigit <= 26:
                dp[i] += dp[i-2]

        # Final answer: ways to decode entire string
        return dp[n]