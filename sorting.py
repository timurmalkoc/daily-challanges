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



def majorityElement(nums):
    d = {}
    majority = []
    for x in set(nums):
        d[x] = nums.count(x)
    appearance = len(nums)/3

    for key, value in d.items():
        if value > appearance:
            majority.append(key)
    
    return majority

print(majorityElement([3,2,3]))


def containsDuplicate(nums):
    nums = sorted(nums)
    for x in range(len(nums)-1):
        if nums[x]==nums[x+1]:
            return True
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))

def merge(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i[0]):
        if out and i[0] <= out[-1][1]:
            out[-1][1] = max(out[-1][1], i[1])
        else:
            out += i,
    return out

print(merge([[1,3],[2,6],[8,10],[15,18]]))
