def check(x,k):
    x.sort()
    n = len(x)
    x.append(0)

    count = 0
    i = 0
    while(i < n):
        j = i
        while(x[j] - x[i] <= k and j < n):
            j +=1
        j -= 1
        count +=1
        i = j + 1
        while(x[i] - x[j] <=k and i < n):
            i+=1
    return count

print(check([1,2,3,4,5],1))