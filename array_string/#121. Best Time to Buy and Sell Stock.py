prices = [7,1,5,3,6,4]

profit, buy, sell = 0, 0, 1

while sell < len(prices):
    diff = prices[sell] - prices[buy]
    profit = max(profit, diff)
    if prices[buy] > prices[sell]:
        buy = sell
    sell += 1
    
print(profit)


cur_max , glob_max = 0, 0

for i in range(1, len(prices)):
    diff = prices[i] - prices[i - 1]
    cur_max = max(cur_max + diff, diff)
    glob_max = max(cur_max, glob_max)
    
print(glob_max)

mn, profit = prices[0], 0

for i in range(1, len(prices)):
    if prices[i] < mn:
        mn = prices[i]
    else:
        profit = max(prices[i] - mn, profit)
        
print(profit)