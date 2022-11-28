def majorityElement(nums):
    majority = -1
    count = 0
    for num in set(nums):
        if nums.count(num) > count:
            majority = num
            count = nums.count(num)
    return majority

print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([3,2,3]))