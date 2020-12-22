def check(x,n,count):
    if(pow(count,n) < x):
        return check(x,n,count+1) + check(x-pow(count,n),n,count+1)
    elif(pow(count,n) == x):
        return 1
    else:
        return 0
        
def powerSum(X, N):
    count = 1
    res = check(X,N,count)
    return res