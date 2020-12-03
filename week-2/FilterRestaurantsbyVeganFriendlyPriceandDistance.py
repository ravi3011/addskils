def check(restaurants, veganFriendly, maxPrice, maxDistance):
    arr = []
    for i,r,vf,p,d in restaurants:
        if(veganFriendly and not vf):
            continue
        
        if(p <= maxPrice and d <= maxDistance):
            arr.append([-r,-i])
            
    arr.sort()
    return [-i for r,i in arr]

print(check([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],0,30,3))    