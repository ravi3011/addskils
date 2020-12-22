def getMinimumCost(k, c):
    temp = [0] * k
    res = 0
    j = 0
    c.sort()
    for i in range(len(c)-1,-1,-1):
        res += (temp[j] + 1)*c[i]
        temp[j] +=1
        j = (j + 1) % k
    return res    
