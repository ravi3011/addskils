import sys
def maxProfit(prices:):
        minp = sys.maxsize
        maxp = 0
        
        for i in range(len(prices)):
            if(prices[i] < minp):
                minp = prices[i]
            elif(prices[i] - minp > maxp):
                maxp = prices[i] - minp
        return maxp 