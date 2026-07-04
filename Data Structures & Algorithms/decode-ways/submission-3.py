class Solution:
    def numDecodings(self, s: str) -> int:
        # 1012 -> 10,12 or 10,1,2
        # i = 0              0               dp[0] = 1
        # i = 1              1               dp[1] = 1
        # i = 2          10                  dp[2] = 1     
        # i = 3            10,1              dp[3] = 1
        # i = 4        10,12   10,1,2        dp[4] = 2
        if not s or s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1) # dp[i] ways to decode using the first ith characters
        dp[0] = 1
        for i in range(1, len(s)+1):
            ch = s[i-1]
            if ch != "0":
                dp[i] = dp[i-1]
            if i >= 2:
                two = s[i-2:i]
                if 10 <= int(two) <= 26:
                    dp[i] += dp[i - 2]
        return dp[len(s)]