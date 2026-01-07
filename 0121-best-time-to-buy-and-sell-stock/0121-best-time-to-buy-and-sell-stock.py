class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        if sorted(prices, reverse = True) == prices:
            return profit
        min_pos = prices.index(min(prices))
        if min_pos == len(prices) - 1:
            min_pos = prices.index(min(prices[:min_pos]))
        profit = max(prices[min_pos:]) - prices[min_pos]
        return profit


        
        """
        :type prices: List[int]
        :rtype: int
        """
        