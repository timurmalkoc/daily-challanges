def reverse(st):
    return ' '.join([x[::-1] for x in st.split(' ')])

print(reverse("Let's take LeetCode contest"))
print(reverse("God Ding"))