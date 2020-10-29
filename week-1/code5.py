def majorityElement(nums):
        d = {}
        for i in nums:
            if(i in d):
                d[i] = d[i] + 1
            else:
                d[i] = 1

        key = 0
        value = -1
        for k,v in d.items():
            if(value < v):
                value = v
                key = k
        return key     