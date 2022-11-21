from typing import List

# DP tabulation
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1 = 0
        step2 = 0
        
        for i in range(2, len(cost)+1):
            curr = step1
            step1 = min(step1 + cost[i-1], step2 + cost[i-2])
            step2 = curr
            
        return step1

# Memoisation
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1 = 0
        step2 = 0
        
        for i in range(2, len(cost)+1):
            curr = step1
            step1 = min(step1 + cost[i-1], step2 + cost[i-2])
            step2 = curr
            
        return step1