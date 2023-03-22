from typing  import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        ans = []
        
        def backtrack(combo, index):
            if len(digits) == len(combo):
                ans.append("".join(combo[:]))
                return # backtrack
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                combo.append(letter)
                # Move on to the next digit
                backtrack(combo, index + 1)
                # Backtrack by removing the letter before moving onto the next
                combo.pop()
                
        backtrack([], 0)
        return ans
                

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mappings = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        letter_lists = []
        for ch in digits:
            letter_lists.append(mappings[ch])
            
        while len(letter_lists) > 1:
            l1 = letter_lists.pop()
            l2 = letter_lists.pop()
            combos = []
            for i in l1:
                for j in l2:
                    combos.append(j + i)
            letter_lists.append(combos)
            
        return [] if not letter_lists else letter_lists[0]
        