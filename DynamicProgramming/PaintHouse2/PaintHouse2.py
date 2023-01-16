from typing import List
from functools import cache
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if len(costs) == 1:
            return min(costs[0])

        k = len(costs[0])

        @cache
        def recurse(n, col):
            if n == len(costs) - 1:
                return costs[n][col]

            cost = float("inf")
            for i in range(k):
                if i == col:
                    continue
                cost = min(cost, recurse(n+1, i))
            return costs[n][col] + cost
        
        cost = float("inf")
        for colour in range(k):
            cost = min(cost, recurse(0, colour))
        return cost