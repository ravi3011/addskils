# import math
# def check(arr,d):
#     n = len(arr)
#     d = d % n
#     g = math.gcd(d,n)

#     for i in range(g):
#         temp = arr[i]
#         j = i
#         while(True):
#             k = j + d
#             if(k >= n):
#                 k = k-n
#             if(k == i):
#                 break
#             arr[j] = arr[k]
#             j = k
#         arr[j] = temp

# arr= [1,2,3,4,5]
# check(arr,4)
# print(arr)

def check(arr,n,k):
    c = 0
    add = 0

    arr.sort()
    for i in range(0,n-1):
        if(add+arr[i] <= k):
            add = add + arr[i]
            c +=1
    return c        

arr = [1,12,5,111,200,1000,10]
n = 7
k = 50
print(check(arr,n,k))    