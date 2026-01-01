prices=[7,1,5,3,6,4]
mini=prices[0]
max_profit=0
for i in range(len(prices)):
    mini=min(mini,prices[i])
    profit=prices[i]-mini
    max_profit=max(max_profit,profit)
print(max_profit)    