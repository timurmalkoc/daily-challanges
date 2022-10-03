import re
def count_accurance(haystack, needle):
    count = len(re.findall(needle,haystack))
    if count>1:
        return haystack.index(needle)
    return -1

print(count_accurance("sadbutsad",'sad'))


def count_jewels(jewels, stones):
    return len([stone for stone in stones if stone in set(jewels)])

print(count_jewels("aA","aAAbbb"))

def count_jewels(jewels, stones):
    return len([stone for stone in stones if stone in set(jewels)])