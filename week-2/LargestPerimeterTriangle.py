def check(A):
    if(not A):
        return 0
    A.sort()
    for i in range(len(A)-3,-1,-1):
        if(A[i] + A[i+1] > A[i+2]):
            return A[i] + A[i+1] + A[i+2]
    return 0

print(check([3,6,2,3]))                