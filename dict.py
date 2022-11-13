def intToRoman(num):
    roman = {1000:"M", 900:"CM", 500:"D", 400:"CD",
                    100:"C", 90:"XC", 50:"L", 40:"XL",
                    10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
    res = ""
    for v in roman.keys():
        res += roman[v] * (num//v)
        num %= v
    return res

print(intToRoman(58))
print(intToRoman(3))
print(intToRoman(1994))