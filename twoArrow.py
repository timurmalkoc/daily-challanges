def maxArea(height):
    res, l, r = 0, 0, len(height)-1 
    while l < r:
        area = min(height[l],height[r]) * (r-l)
        res = max(area, res)
        if height[l] > height[r]:
            r -=1
        else:
            l +=1
    return res 

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))