def reverse(st):
    return ' '.join([x[::-1] for x in st.split(' ')])

print(reverse("Let's take LeetCode contest"))
print(reverse("God Ding"))


def longestPalindrome(s):
        pal = ''
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if s[i:j] == s[i:j][::-1] and len(pal)<j-i:
                    pal = s[i:j]
        return pal


print(longestPalindrome("babb"))
print(longestPalindrome("abcd"))