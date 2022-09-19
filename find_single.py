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