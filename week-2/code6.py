def check(n):
    count = 0
    while(n):
        
        print("checking even odd-",n & 1)
        count += n & 1
        print("n is decresing -",n>>1)
        n >>= 1
        
    return count

print(check(11))        