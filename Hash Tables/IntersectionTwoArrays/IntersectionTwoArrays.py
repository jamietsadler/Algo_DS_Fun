from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        for i in range(len(nums1)):
            if nums1[i] in hashmap:
                hashmap[nums1[i]] += 1
            else:
                hashmap[nums1[i]] = 1
                
        result = []
        
        for j in range(len(nums2)):
            if nums2[j] in hashmap and hashmap[nums2[j]] > 0:
                result.append(nums2[j])
                hashmap[nums2[j]] -= 1
        
        return result
                
                