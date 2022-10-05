# The power of lambda is better shown when you use them as an anonymous function inside another function.

# A lambda function can take any number of arguments, but can only have one expression
# lambda arguments : expression

x = lambda a : a + 10 #
print(x(5)) # 15 passing the argument like without using the object

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) # 13


### With filter
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)