import collections import OrderedDict

def printView(root,height,hd,d):
    if(root is None):
        return
    if(hd not in d):
        d[hd] = [root.info,height]
    else:
        p = d[hd]
        if(p[1] > height):
            d[hd] = [root.info,height]
    printView(root.left,height+1,hd-1,d)
    printView(root.right,height+1,hd+1,d)

def topView(root):
    #Write your code here
    d = OrderedDict()
    
    printView(root,0,0,d)
    
    for i in sorted(list(d)):
        p = d[i]
        print(p[0],end=" ")
    print()    