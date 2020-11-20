def searchInsert(nums, target):
    if(len(nums) == 0):
        return 0
    if(len(nums) == 1):
        if(nums[0] == target):
            return 0
        elif(nums[0] > target):
            return 0
        elif(nums[0] < target):
            return 1
    i = 0
    j = len(nums)-1
    pos = -1
    while(i <= j):
        mid = i + (j-i)//2

        if(nums[mid] == target):
            return mid
        elif(nums[mid] > target):
            j = mid -1
            pos = mid
        else:
            i = mid + 1
            pos = mid + 1
    return pos                


nums = [7]
print(searchInsert(nums, 7))