from typing import List, defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        fm = defaultdict(int)
        count = 0

        for a in nums1:
            for b in nums2:
                fm[a+b] += 1
        
        for c in nums3:
            for d in nums4:
                count += fm[-(c+d)]

        return count