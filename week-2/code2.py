def checkRotationIndex(arr,start,end):
    if(end < start):
        return -1
    if(end == start):
        return start
    while(start <= end):
        mid = start + (end - start) // 2

        if(mid < end and arr[mid+1] < arr[mid]):
            return mid+1
        if(mid > start and arr[mid] < arr[mid-1]):
            return mid

        if(arr[end] > arr[mid]):
            end = mid - 1
        else:
            start = mid + 1                   
    return -1


def search(arr,value,start,end):
    if(end < start):
        return -1
    if(len(arr) == 1 and arr[0] == value):
        return 0
    if(len(arr) == 1 and arr[0] != value):
        return -1

    while(start < end):
        mid = start + (end - start) // 2

        if(arr[mid] == value):
            return mid
        elif(arr[mid] < value):
            start = mid + 1
        else:
            end = mid - 1
    return -1                            


arr = [1,3]
midd = checkRotationIndex(arr,0,len(arr)-1)
print(midd)
if(midd == -1):
    print("no target element")
else:
    r = search(arr,1,midd-1,len(arr)-1)
    l = search(arr,1,0,midd-1)
    print(r," ",l)
    if(l != -1 ):
        print(l)
    elif(r != -1):
        print(r)
    else:
        print("no element found")             
