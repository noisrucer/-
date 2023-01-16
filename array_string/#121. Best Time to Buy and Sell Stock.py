prices = [7,1,5,3,6,4]

profit, buy, sell = 0, 0, 1

while sell < len(prices):
    diff = prices[sell] - prices[buy]
    profit = max(profit, diff)
    print(max(profit, diff))
    if prices[buy] > prices[sell]:
        buy = sell
    sell += 1
    
print(profit)