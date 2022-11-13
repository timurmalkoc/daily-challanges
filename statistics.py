def findMedianSortedArrays(nums1, nums2):
    all = sorted(nums1+nums2)
    if(len(all)%2==1):
        return all[len(all)//2]
    else:
        return (all[(len(all)//2)-1] + all[(len(all)//2)])/2.0

print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1,2], [3,4]))