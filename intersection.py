def intersection(nums1, nums2):
    return set(nums1) & set(nums2)

print(intersection([1,2,2,1], [2, 2]))
print(intersection([4,9,5], [9,4,9,8,4]))

def missingNumber(nums):
    nums = sorted(nums)
    for x in range(0,len(nums)):
        if x != nums[x]:
            return x
    return nums[-1]+1

print(missingNumber([1, 2, 3]))
print(missingNumber([0, 3, 1, 4]))