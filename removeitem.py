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
