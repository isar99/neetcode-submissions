# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buy = min(prices)
#         for i in range(len(prices)):
#             if prices[i] == buy:
#                 new_prices = prices[i:]
#         sale = max(new_prices)
#         return sale - buy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        maxP = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
            else:
                buy = sell
            sell += 1
        return maxP


        
            
        