def check(n,arr):
    d = {}
    for i in range(n):
        if( arr[i] in d):
            d[arr[i]].append(i)
        else:
            d[arr[i]] = [i]
    res = [i for _,i in d.items()]
    add = 0
    for e in res:
        add += e[-1] - e[0]        
    print(add)            



t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    check(n,arr)


# def check(strList):
#     n= len(strList)
#     d = {}

#     for i in range(n):
#         temp = strList[i]
#         s = ''.join(sorted(strList[i]))
#         if(s in d):
#             d[s].append(temp)
#         else:
#             d[s] = [temp]
#     return [e for _,e in d.items()] 

# print(check(['eat','tea','tan','ate','nat','bat']))                
