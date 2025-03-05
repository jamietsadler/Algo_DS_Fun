
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        indexes = []
        result = ''
        stack = []
        for i, char in enumerate(s):
            if char != '(' and char != ')':
                continue
            elif char == ')' and not stack:
                indexes.append(i)
            elif char == ")":
                stack.pop()
            else:
                stack.append(i)

        for i, char in enumerate(s):
            if i not in stack and i not in indexes:
                result += char

        return result
            