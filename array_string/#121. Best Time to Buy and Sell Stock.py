# my solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy, sell = 0, 0, 1

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                if profit < prices[sell] - prices[buy]:
                    profit = prices[sell] - prices[buy]
            sell += 1

        return profit
    
# another solution
class Solution:
    def maxProfit(self, prices):
        profit, buy, sell = 0, 0, 1
        while sell < len(prices):
            diff = prices[sell] - prices[buy]
            profit = max(profit, diff)
            if prices[buy] > prices[sell]:
                buy = sell
            sell += 1
        return profit