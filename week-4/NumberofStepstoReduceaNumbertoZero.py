
def check(num):
    step = 0
    while(num > 0):
        if(num & 1 == 0):
            num >>= 1
            #print(num)
            step += 1
        else:
            num -= 1
            step += 1
    return step
print(check(123))                
