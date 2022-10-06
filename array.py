def add_one(lst):
    return [x for x in str(int(''.join([str(n) for n in lst]))+1)]


print(add_one([4,3,2,1]))


def find_non_repeat(st):
    d = {}
    for i in st:
        if i in d:
            d[i] += 1 
        else:
            d[i] = 1

    for index, val in enumerate(st):
        if d[val] == 1:
            return index
    else:
        return -1

print(find_non_repeat("leetcode"))
print(find_non_repeat("loveleetcode"))
print(find_non_repeat("aabb"))