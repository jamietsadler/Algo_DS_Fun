class Solution(object):
    def maxProfit(self, prices, fee):
        
        profit_so_far_if_we_sell = 0
        profit_so_far_if_we_buy = profit_so_far_if_we_sell - prices[0]
        
        for i in range(1, len(prices)):
            profit_so_far_if_we_sell = max(profit_so_far_if_we_sell, profit_so_far_if_we_buy + prices[i] - fee)
            profit_so_far_if_we_buy  = max(profit_so_far_if_we_buy, profit_so_far_if_we_sell - prices[i])
        
        return profit_so_far_if_we_sell