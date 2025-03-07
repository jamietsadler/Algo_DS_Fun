
from collections import defaultdict, heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        heap = []
        for freq in count.values():
            heapq.heappush(heap, freq)
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = [key for key, val in count.items() if val in heap]
        return ans