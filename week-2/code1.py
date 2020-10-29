# find first and last position of element in sorted array

def getIndex(arr,value,start,end,flag):
    res = -1

    while(start <= end):
        mid = start + (end - start) // 2
        if(arr[mid] == value):
            res = mid
            if(flag == True):
                end = mid-1
            else:
                start = mid + 1    
        elif(arr[mid] < value):
            start = mid + 1
        else:
            end = mid - 1
    return res

arr = [5,7,7,9]
print(getIndex(arr,7,0,len(arr)-1,True))
print(getIndex(arr,7,0,len(arr)-1,False))                    