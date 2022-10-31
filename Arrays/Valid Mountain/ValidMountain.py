from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        increased = False
        decreased = False
        
        if len(arr) < 3:
            return False
        
        for i in range(1, len(arr)):
            if decreased == False and arr[i] > arr[i-1]:
                increased = True
            elif increased and decreased == False and arr[i] < arr[i-1]:
                decreased = True
            elif increased and decreased and arr[i] < arr[i-1]:
                pass
            else:
                return False
        if increased and decreased:
            return True
        else:
            return False