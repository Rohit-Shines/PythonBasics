string_value = "alphanumeric@123__"
s = ''.join(filter(str.isalnum, string_value))

print(s)
