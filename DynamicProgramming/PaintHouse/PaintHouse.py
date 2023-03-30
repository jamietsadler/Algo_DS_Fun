from typing import List
from functools import cache
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 1:
            return min(costs[0])
        
        @cache
        def recurse(n, col):
            total_cost = costs[n][col]
            if n == len(costs) - 1:
                pass
            elif col == 0:
                total_cost += min(recurse(n+1, 1), recurse(n+1, 2))
            elif col == 1:
                total_cost += min(recurse(n+1, 0), recurse(n+1, 2))
            else:
                total_cost += min(recurse(n+1, 1), recurse(n+1, 0))
            return total_cost
        
        return min(recurse(0, 0), recurse(0,1), recurse(0,2))

# bottom up (in place)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 1:
            return min(costs[0])

        dp = [[0]*3 for _ in range(len(costs)+1)]

        for i in range(len(costs)-2, -1, -1):
            costs[i][0] = costs[i][0] + min(costs[i+1][1], costs[i+1][2])
            costs[i][1] = costs[i][1] + min(costs[i+1][0], costs[i+1][2])
            costs[i][2] = costs[i][2] + min(costs[i+1][0], costs[i+1][1])

        return min(costs[0])

# Bottom up, separate matrix
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 1:
            return min(costs[0])

        dp = [[0]*3 for _ in range(len(costs)+1)]
        print(dp)
        for i in range(len(costs)-1, -1, -1):
            dp[i][0] = costs[i][0] + min(dp[i+1][1], dp[i+1][2])
            dp[i][1] = costs[i][1] + min(dp[i+1][0], dp[i+1][2])
            dp[i][2] = costs[i][2] + min(dp[i+1][0], dp[i+1][1])

        return min(dp[0])
