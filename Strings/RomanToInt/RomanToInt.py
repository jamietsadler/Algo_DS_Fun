class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mappings = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0 
        total = 0
        while i < len(s):
            if i < len(s) -1:
                if mappings[s[i]] < mappings[s[i+1]]:
                    total += mappings[s[i+1]] - mappings[s[i]]
                    i += 2
                else:
                    total += mappings[s[i]]
                    i += 1
            else:
                    total += mappings[s[i]]
                    i += 1
        return total