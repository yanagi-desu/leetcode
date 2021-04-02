from typing import List
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = []
        stack.append(-1)
        for i, j in enumerate(s):
            if j == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans,i-stack[-1])
        return ans
sovle = Solution()
print(sovle.longestValidParentheses(")()())"))