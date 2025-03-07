class Solution(object):
    def validPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def check_pal(i, j):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            
            else:
                return check_pal(i, j-1) or check_pal(i+1, j)
        return True
