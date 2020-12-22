class Solution:
    def insert(self,intervals,newInterval):
        intervals += [newInterval]
        print(intervals)
        intervals.sort()
        merge = []
        for interval in intervals:
            if not merge or merge[-1][1] < interval[0]:
                merge.append(interval)
            else:
                merge[-1][1] = max(merge[-1][1], interval[1])
        return merge


s = Solution()

print(s.insert([[1,3],[6,9]],[2,5]))
