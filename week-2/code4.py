def mySqrt(x):
    if(x == 0 or x == 1):
        return x

    start = 1
    end = x
    res = 1
    while(start <= end):
        mid = start + (end - start) // 2
        if(mid * mid == x):
            return mid
        elif(mid * mid < x):
            start = mid + 1
            res = mid
        else:
            end = mid - 1
    return res 

print(mySqrt(9))                       