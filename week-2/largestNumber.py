class Num(str):
    def __lt__(x,y):
        return x+y > y+x

class Solution:        
    def largestNumber(self, nums):
        large = ''.join(sorted(map(str,nums),key=Num))
        print(sorted(map(str,nums),key=Num))
        print(large)
        if(large[0] == '0'):
            return '0'
        else:
            return large    

s = Solution()
print(s.largestNumber([3,39]))            