class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1*stone)

        while len(heap) > 1:
            stone1 = -1 * heapq.heappop(heap)
            stone2 = -1 * heapq.heappop(heap)

            if stone1 == stone2:
                continue
            else:
                rem = abs(stone1-stone2)
                heapq.heappush(heap, -1 * rem)

        if len(heap) == 0:
            return 0
        else:
            return -1*heapq.heappop(heap)
