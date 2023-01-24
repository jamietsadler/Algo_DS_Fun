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
                