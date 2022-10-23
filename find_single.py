import time
# Given a non-empty array of integers nums, every element appears twiceexcept for one. Find that single one.
# BONUS: You must implement a solution with a linear runtime complexity and use only constant extra space.
st = time.time()

def get_sigle_item(lst):
    for item in lst:
        if lst.count(item) == 1:
            return item    


print(get_sigle_item([4,1,2,1,2]))
print(get_sigle_item([2,2,1]))
print(get_sigle_item([1]))

print("Execution time = ", time.time()-st)

# find index of target number

def find_index(lst, target):
    return lst.index(target) if lst.count(target) else -1



print(find_index([-1,0,3,5,9,12],5))


# find index of target number by binary

def find_index2(lst, target):

    low = 0
    high = len(lst)

    while low<=high:
        mid = (low+high)//2
        # if target greater, ignore left half
        if lst[mid] < target:
            low = mid + 1
        # if target lower, ignore right half
        elif lst[mid] > target:
            high = mid - 1
        # if mid index points target value, return index of target
        else:
            return mid
    # if the element was not fount 
    return -1



print(find_index2([-1,0,3,5,9,12],4))


def recursive_find(lst, target, low, high):
    if low <= high: 
        mid = (low+high)//2

        if lst[mid] == target:
            return mid

        if lst[mid] < target:
            return recursive_find(lst, target, mid+1, high)
        else:
            return recursive_find(lst, target, low, mid-1)
    return -1

lst = [-1,0,3,5,9,12]

print(recursive_find(lst, 3, 0, len(lst)))

def firstMissingPositive(nums):
    positives = sorted([x for x in nums if x>0])
    for x,val in enumerate(positives, start=1):
        if x!=val:
            return x
    else:
        return x+1

print("firstMissingPositive")
print(firstMissingPositive([3,4,-1,1]))
print(firstMissingPositive([7,8,9,11,12]))
print(firstMissingPositive([1,2,0]))