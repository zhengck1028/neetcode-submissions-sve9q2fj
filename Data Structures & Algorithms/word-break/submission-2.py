class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n + 1):
            for word in wordDict:
                l = len(word)
                if i >= l and s[i-l:i] == word:
                    dp[i] = dp[i] or dp[i-l]
        return dp[n]