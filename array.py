def add_one(lst):
    return [x for x in str(int(''.join([str(n) for n in lst]))+1)]


print(add_one([4,3,2,1]))