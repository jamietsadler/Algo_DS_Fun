from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash_tab = {}
        for n in arr:
            if n*2 in hash_tab or n/2 in hash_tab:
                return True
            else:
                hash_tab[n] = n
        return False