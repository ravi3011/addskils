from collections import Counter
def check(arr,brr):
    l1 = Counter(arr)
    l2 = Counter(brr)
    temp = []
    for k,v in l2.items():
        if(not k in l1):
            temp.append(k)
        elif(k in l1 and v > l1[k]):
            temp.append(k)
    print(sorted(temp))        


check([203,204,205,206,207,208,203,204,205,206],[203,204,204,205,206,207,205,208,203,206,205,206,204])    
