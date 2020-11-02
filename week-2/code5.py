def merge(intervals):
        if(not intervals):
            return []
        
        if(len(intervals) == 1):
            return intervals
        intervals.sort()
        s,e = intervals[0]

        
        l = []
        for i , j in intervals:
            if(e >= i):
                if(i <= s):
                    s = i
                if(j >= e):
                    e = j
            else:
                l.append([s,e])
                s,e = i,j
        l.append([s,e])
        return l


print(merge([[1,4],[2,3]])) 