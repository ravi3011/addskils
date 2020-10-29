
#this is the recursive way of binary search
def search(arr,value,start,end):
    
    if(end > start):
        mid = int(start + (end - start)//2)

        if(arr[mid] == value):
            return mid
        elif(arr[mid] > value):
            return search(arr,value,start,mid-1)
        elif(arr[mid] < value):
            return search(arr,value,mid+1,end)
    else:
        return -1

arr = [1,2,3,4,5,7,8]
value = 7
#print(search(arr,value,0,len(arr)))  

#iteravtive way of binary search