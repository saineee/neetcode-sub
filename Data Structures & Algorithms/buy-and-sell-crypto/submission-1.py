class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       min_price = prices[0]
       max_profit = 0
       for i in range(len(prices)):
           max_profit = max(prices[i] - min_price, max_profit)
           min_price = min(prices[i], min_price)
       return max_profit