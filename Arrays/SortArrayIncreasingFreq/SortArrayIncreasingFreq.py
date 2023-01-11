import collections
from typing import List
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        print(count)
        return sorted(nums, key = lambda n: (count[n], -n))