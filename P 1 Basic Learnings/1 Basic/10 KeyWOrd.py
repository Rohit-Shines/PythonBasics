

# # If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# #
# # The global keyword makes the variable global.
# def myfunc():
#   global x
#   x = 300
#
# myfunc()
#
# print(x)

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])