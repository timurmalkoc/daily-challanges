def sortColors(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
    return nums

print(sortColors([2,0,2,1,1,0]))
print(sortColors([2,0,1]))


def findKthLargest(nums, k):
    return sorted(nums, reverse=True)[k-1]

print(findKthLargest([3,2,1,5,6,4], 2))
print(findKthLargest([3,2,3,1,2,4,5,5,6], 1))