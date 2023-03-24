
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        maxLength = 0

        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                maxLength = max(maxLength, 2 * right)
            elif right >= left:
                left = 0
                right = 0

        left = 0
        right = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                maxLength = max(maxLength, 2 * left)
            elif left >= right:
                left = 0
                right = 0

        return maxLength


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0

        for i in range(len(s)):
            if s[i] == ")":
                stack.pop()
                if stack:
                    ans = max(ans, i - stack[-1])
                    continue
            stack.append(i)

        return ans


