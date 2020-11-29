def gameOfThrones(s):
    check = True
    count = 0
    wordcount = [0] *26
    
    for l in s:
        wordcount[ord(l)- ord('a')] +=1
    for c in wordcount:
        count += c % 2
    if(count > 1):
        check = False 
    if(not check):    
        return "NO"
    else:
        return "YES"
    