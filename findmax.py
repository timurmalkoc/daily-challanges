from re import X


def find_max(lst):
    x = lst[0]
    for left_pointer in range(len(lst)):
        for rigth_pointer in range(left_pointer,len(lst)):
            if x < sum(lst[left_pointer:(rigth_pointer+1)]):
                #print(lst[left_pointer:rigth_pointer])
                x = sum(lst[left_pointer:(rigth_pointer+1)])
    return x


print(find_max([-2,1,-3,4,-1,2,1,-5,4]))
print(find_max([1]))
print(find_max([5,4,-1,7,8]))

def find_max2(lst):
    mx = lst[0]
    for pointer in range(1,len(lst)):
        if mx > pointer:
            mx += pointer
        else:
            mx = pointer
            
    return mx

print(find_max([-2,1,-3,4,-1,2,1,-5,4]))
print(find_max([1]))
print(find_max([5,4,-1,7,8]))