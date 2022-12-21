def findMin(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (high + low) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    return nums[low]

print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))