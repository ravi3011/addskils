import heapq
def check(k,a):
    temp = []
    n = len(a)

    for i in range(n):
        heapq.heappush(temp,a[i])
    count = 0

    while(len(temp) > 1 and heapq.nsmallest(1,temp)[0] < k):
        a1 = heapq.heappop(temp)
        b1 = heapq.heappop(temp)
        count +=1
        heapq.heappush(temp,(a1*1+b1*2))
    if(heapq.nsmallest(1,temp)[0] < k):
        return -1
    return count

print(check(7,[1,2,3,9,10,12]))        
