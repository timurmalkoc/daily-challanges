def closeStrings(word1, word2):
    d1 = {}
    d2 = {}
    for x in word1:
        if not x in d1:
            d1[x] = 1
        else:
            d1[x] +=1
            
    for x in word2:
        if not x in d2:
            d2[x] = 1
        else:
            d2[x] +=1
    
    if sorted(d1.keys()) != sorted(d2.keys()) or sorted(d1.values()) != sorted(d2.values()):
        return False

    return True

print(closeStrings("abc", "acb"))
print(closeStrings("abc", "acc"))