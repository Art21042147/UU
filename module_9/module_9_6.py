def all_variants(text):
    length = len(text)
    for char in range(1, length + 1):
        for index in range(length - char + 1):
            yield text[index:index + char]


a = all_variants("abc")
for i in a:
    print(i)
