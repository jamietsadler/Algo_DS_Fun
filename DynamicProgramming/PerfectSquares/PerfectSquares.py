import math 
from collections import deque
# Recursive approach (long runtime)
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]

        def minNumSquares(k):
            """ recursive solution """
            # bottom cases: find a square number
            if k in square_nums:
                return 1
            min_num = float('inf')

            # Find the minimal value among all possible solutions
            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquares(k-square) + 1
                min_num = min(min_num, new_num)
            return min_num

        return minNumSquares(n)

# DP, Bottom up
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]

        dp = [float("inf")] * (n+1)

        dp[0] = 0
        for i in range(n+1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square]+1)

        return dp[-1]

# Greedy and BFS
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]

        level = 0
        queue = deque([(n, 1)])

        while queue:
            for _ in range(len(queue)):
                remainder, level = queue.popleft()
                for square in square_nums:
                    if remainder == square:
                        return level
                    elif remainder < square:
                        break
                    else:
                        queue.append((remainder - square, level+1))
        
        return level
