def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        temp = {}
        
        for i in s:
            if( i in temp):
                temp[i] +=1
            else:
                temp[i] = 1
        for i in t:
            if(i not in temp):
                return False
            temp[i] -= 1
                
            if(temp[i] < 0):
                return False
        return True  