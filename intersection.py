def intersection(nums1, nums2):
    return set(nums1) & set(nums2)

print(intersection([1,2,2,1], [2, 2]))
print(intersection([4,9,5], [9,4,9,8,4]))