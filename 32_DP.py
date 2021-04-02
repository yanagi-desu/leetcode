class Solution:
    def longestValidParentheses(self, s: str) -> int:   
        dp = [0]*len(s)
        for i in range(len(s)):
            if s[i]==")":
                if i-1>=0 and s[i-1] == "(":
                    if i>=2:
                        dp[i] = 2+dp[i-2]
                    else:
                        dp[i] = 2
                elif i-dp[i-1]>0 and s[i-dp[i-1]-1] == "(":
                    if i-dp[i-1]>=2:
                        dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
                    else:
                        dp[i] = dp[i-1]+2
        return max(dp) if dp else 0

solve = Solution()
print(solve.longestValidParentheses("()(())"))

