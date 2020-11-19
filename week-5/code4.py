def bs(arr,low,high,k):
    if(high >= low):
        mid = low + (high - low) // 2
        if(k == arr[mid]):
            return mid
        elif(k > arr[mid]):
            return bs(arr,mid+1,high,k)
        else:
            return bs(arr,low,mid-1,k)
    return -1    

def pairs(k, arr):
    arr.sort()
    count = 0
    n = len(arr)
    for i in range(0,n-1):
        if(bs(arr,i+1,n-1,arr[i] + k) != -1):
            count +=1
    return count 

print(pairs(2,[1,3,5,8,6,4,2]))    