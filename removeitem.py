# https://leetcode.com/problems/remove-element/
def removeElement(nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i


def comp(nums, val):
    return len([x for x in nums if x!=val])

print(removeElement([3,2,2,3],3))
print(comp([3,2,2,3],3))


# ==============================================
# https://leetcode.com/problems/search-insert-position/
def searchInsert(nums, target):
        for x in range(len(nums)):
            if nums[x]>=target:
                return x
        else:
            return x+1

print(searchInsert([1,3,5,6],5))