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

print('================')

def max_subarray(lst):
    count = 1
    max = 0
    diff = 0
    for i in range(1,len(lst)):
        count = 1
        max = 1
        if len(lst)<2:
            return max

        diff = lst[1]-lst[0]
        for i in range(1,len(lst)):
            if diff > 0 and lst[i]-lst[i-1] == diff:
                count += 1
            else:
                if count > max:
                    max = count
                diff = lst[i]-lst[i-1]
                count = 1
                if diff>0:
                    count=2
                print(diff)
        else:
            if count > max:
                max = count
        return max

print(max_subarray([1,3,5,4,7]))
print(max_subarray([2,2,2,2,2]))
print(max_subarray([1,3,5,4,2,3,4,5]))
        


def DividingNumbers(left, right):
        
    def divisible(n):
        for d in str(n):
            if d == '0' or n % int(d) > 0:
                return False
        return True
    
    
    res = []
    for n in range(left, right + 1):
        if divisible(n):
            res.append(n)
    return res


print(DividingNumbers(1,22))