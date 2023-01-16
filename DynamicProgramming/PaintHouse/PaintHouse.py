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