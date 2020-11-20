def findTheDifference(self, s: str, t: str) -> str:
        d1 = {}
        for e in s:
            if(e in d1):
                d1[e] +=1
            else:
                d1[e] = 1
        d2 = {}
        for e in t:
            if(e in d2):
                d2[e] += 1
            else:
                d2[e] = 1
                
        for e in t:
            if(e not in d1):
                return e
            elif(d1[e] != d2[e]):
                return e
        