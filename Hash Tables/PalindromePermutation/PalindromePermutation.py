class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        # add all odd occurences, should ne less than 1 at end if palindrome exists
        unpaired = set()

        for char in s:
            if char not in unpaired:
                unpaired.add(char)
            else:
                unpaired.remove(char)

        return len(unpaired) <= 1