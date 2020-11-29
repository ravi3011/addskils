import sys

def check():
    n = int(input())
    res = []
    max = []
    for i in range(n):
        arr = list(map(int,input().strip().split()))
        if(arr[0] == 1):
            res.append(arr[1])
            if(max == [] or arr[1] >= max[-1] ):
                max.append(arr[1])

        elif(arr[0] == 2):
            t = res.pop()
            if(t == max[-1]):
                max.pop()
            
        else:
            if(max):
                print(max[-1])
              


check()