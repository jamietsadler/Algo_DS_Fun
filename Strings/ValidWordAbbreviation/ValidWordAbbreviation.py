
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isnumeric():
                k = j
                while k < len(abbr) and abbr[k].isnumeric():
                   
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False


        return i == len(word) and j == len(abbr)

            


