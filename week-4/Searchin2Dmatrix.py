def check(arr,key,n,m):
    i = 0
    j = len(arr) - 1

    while(i >= 0 and i < n and j >= 0 and j < m):
        if(arr[i][j] == key):
            return True

        elif(arr[i][j] > key):
            j -= 1
        elif(arr[i][j] < key):
            i += 1
    return False

arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(check(arr,13,4,3))                    