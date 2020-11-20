def firstUniqChar(self, s: str) -> int:
        has = {}
        for e in s:
            if(e in has):
                has[e] += 1
            else:
                has[e] = 1
        for i in range(len(s)):
            if(has[s[i]] == 1):
                return i
                break
                
        return -1    