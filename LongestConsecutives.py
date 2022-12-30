def longestConsecutive(nums):
    s, longest = set(nums), 0
    for num in s:
        if num - 1 in s: continue
        j = 1
        while num + j in s: j += 1
        longest = max(longest, j)
    return longest

print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))