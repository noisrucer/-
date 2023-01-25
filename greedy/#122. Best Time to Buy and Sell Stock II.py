'''
TC: O(n)
SC: O(1)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0] # idx
        max_profit = 0

        for e in prices[1:]:
            if e > buy:
                max_profit += (e - buy)
                buy = e
            else:
                buy = e

        return max_profit
