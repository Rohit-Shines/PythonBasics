import collections

# counter for list
# create a list
numbers = [2, 3, 5, 2, 11, 2, 7]
x = numbers.count(2) # there are 3 twos here
print(x) # 3


# counter for strings
a="apple"
count=collections.Counter(a)
print(count) # Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})