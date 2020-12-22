class Solution:
    def trap(self, height: List[int]) -> int:
        if(not height):
            return 0
        size = len(height)
        maxl = [0] * size
        maxr = [0] * size

        maxl[0] = height[0]
        for i in range(1,size):
            maxl[i] = max(maxl[i-1],height[i])
        # print(maxl)
        maxr[size-1] = height[-1]
        for i in range(size-2,-1,-1):
            maxr[i] = max(maxr[i+1],height[i])
        # print(maxr)
        res = 0
        for i in range(size):
            res += (min(maxl[i],maxr[i]) - height[i])
        return res