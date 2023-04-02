from typing import List

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]
        return total

# Only 2 purchases, DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right_profits = [0] * (len(prices) + 1)
        left_profits = [0] * len(prices)
        left_min = prices[0]
        right_max = prices[-1]

        for i in range(1, len(prices)):
            left_profits[i] = max(left_profits[i-1], prices[i] - left_min)
            left_min = min(left_min, prices[i])
            
        for i in range(len(prices)-1, 0, -1):
            right_profits[i] = max(right_profits[i+1], right_max - prices[i])
            right_max = max(right_max, prices[i])

        max_total = 0
        for i in range(len(prices)):
            max_total = max(max_total, left_profits[i] + right_profits[i+1])
        return max_total

# Only 2 purchases, one pass
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit

# K transactions
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0: return 0

        d = [[float('inf'),0] for _ in range(k+1)] # [[cost, profit]...]

        for price in prices:
            for i in range(1, k+1):
                # minimize the cost when buying - reinvest the profit from previous transaction
                d[i][0] = min(d[i][0], price-d[i-1][1])
                # maximize the profit when selling - use the minimum cost you incurred in past
                d[i][1] = max(d[i][1], price-d[i][0])

        return d[-1][1]