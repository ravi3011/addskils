def longestCommonPrefix(strs):
        if(len(strs) == 0):
            return ""
        p = strs[0]
        for i in range(1,len(strs)):
            while(strs[i].find(p) != 0):
                p = p[0:len(p)-1]
                if(len(p) == 0):
                    return ""
        return p
        