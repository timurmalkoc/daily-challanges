def find_lenght_of_last_word(s):
    return (len(s.split()[-1]))


print(find_lenght_of_last_word("Hello World"))

def find_lenght_of_last_word2(s):
    s = s.rstrip()
    c = 0
    for x in range(len(s)-1,-1,-1):
        if s[x] == ' ':
            return c
        c += 1
    else:
        return c

print(find_lenght_of_last_word2("Hello World"))