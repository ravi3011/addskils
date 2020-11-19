def checkElement(arr):
    s = []
    res = [0 for i in range(len(arr))]

    for i in range(len(arr)-1,-1,-1):
        while(len(s) > 0 and s[-1] <= arr[i]):
            s.pop()

        if(len(s) == 0):
            res[i] = -1
        else:
            res[i] = s[-1]

        s.append(arr[i])

    arr[::-1]   
    for i in range(len(arr)-1,-1,-1):
        while(len(s) > 0 and s[-1] <= arr[i]):
            s.pop()

        if(len(s) == 0):
            res[i] = -1
        else:
            res[i] = s[-1]

        s.append(arr[i])    
    # for i in range(len(res)):    
    #     if(res[i] > arr[-1]):
    #         res[-1] = res[i]
    #         break

    return res

print(checkElement([1,2,1]))        