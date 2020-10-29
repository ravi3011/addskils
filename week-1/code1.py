
def twoSum(nums, target):
    d = {}
    res = []
    for i in range(len(nums)):
        temp = target - nums[i]
        if(temp in d):
            res = [d[temp],i]
        else:    
            d[nums[i]] = i
    
    return res   