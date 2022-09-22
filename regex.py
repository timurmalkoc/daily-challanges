import re
def count_accurance(haystack, needle):
    count = len(re.findall(needle,haystack))
    if count>1:
        return haystack.index(needle)
    return -1

print(count_accurance("sadbutsad",'sad'))
