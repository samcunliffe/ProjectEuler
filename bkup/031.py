
# http://www.algorithmist.com/index.php/Coin_Change

coins=range(1,99)
count=[0]*101

count[0]=1
for coin in coins:
    #print coin
    for i in range(coin,101):
        count[i]+=count[i-coin]
    #print count[1:]

print count[100]
