class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def helper(first, second):
            if first > second:
                return
            s[first], s[second] = s[second], s[first]
            helper(first + 1, second - 1)
        
        helper(0, len(s) -1 )