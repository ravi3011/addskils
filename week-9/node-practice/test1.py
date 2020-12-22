import heapq

def addnum(num,minheap,maxheap):
    if(not maxheap or num < -maxheap[0]):
        heapq.heappush(maxheap,-num)
    else:
        heapq.heappush(minheap,num)

def balance(minheap,maxheap):
    if(len(minheap) - len(maxheap) >= 2):
        heapq.heappush(maxheap,-heapq.heappop(minheap))
    if(len(maxheap) - len(minheap) >= 2):
        heapq.heappush(minheap,-heapq.heappop(maxheap))

def getMedian(minheap,maxheap):
    if(len(minheap) == len(maxheap)):
        return (minheap[0] - maxheap[0])/2
    elif(len(minheap) > len(maxheap)):
        return float(minheap[0])
    else:
        return float(-maxheap[0])                

def check(a):
    minheap = []
    maxheap = []
    res = []
    for num in a:
        addnum(num,minheap,maxheap)
        balance(minheap,maxheap)
        res.append(getMedian(minheap,maxheap))
check([12,4,5,3,8,7])



# def waiter(number, q):
    
#     primeNum = [1] * 10000
#     prime = []
#     for i in range(2,10000):
#         if(primeNum[i] == 1):
#             for j in range(i,10000,i):
#                 primeNum[j] = 0
#             prime.append(i)
            
#     A = [[] for i in range(q+1)]
#     B = [[] for i in range(q+1)]
    
#     A[0] = number
    
#     for i in range(q):
#         while(A[i]):
#             p = A[i].pop()
#             if(p % prime[i] == 0):
#                 B[i+1].append(p)
#             else:
#                 A[i+1].append(p)
                
#     res = []
#     for i in range(q+1):
#         while(B[i]):
#             res.append(B[i].pop())
#     for i in range(q+1):
#         while(A[i]):
#             res.append(A[i].pop())
#     return res