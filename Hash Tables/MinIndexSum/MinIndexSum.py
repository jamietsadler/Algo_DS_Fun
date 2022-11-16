from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map = {}
        result = {}
        
        for i, string in enumerate(list1):
            hash_map[string] = i
            
        for j, string in enumerate(list2):
            if string in hash_map:
                key = j + hash_map[string]
                if key in result:
                    result[key].append(string)
                else:
                    result[key] = [string]
                    
                    
        min_value = float('inf')
        for key in result.keys():
            min_value = min(min_value, key)
        if min_value == float('inf'):
            return None
        return result[min_value]