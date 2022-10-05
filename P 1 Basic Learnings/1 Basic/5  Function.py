



# # Python also accepts function recursion, which means a defined function can call itself.
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)


# # put in the pass statement to avoid getting an error. as the function is empty
# def myfunction():
#   pass

##To let a function return a value, use the return statement:
# def my_function(x):
#   print(5*x)
#   return 5*x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))


# # You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# def my_function(food):
#   for x in food:
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)


# # If we call the function without argument, it uses the default value:
# def my_function(country = "Norway"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# # If the number of keyword arguments is unknown, add a double ** before the parameter name:
# def my_function(**kid):
#   print("His last name is " + kid["fname"]+kid["lname"])
#
# my_function(fname = "Tobias", lname = "Refsnes")


# # This way the order of the arguments does not matter.
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
#
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# interesting way of passing argument with minimal code
# If the number of arguments is unknown, add a * before the parameter name:
# def my_function(*kids):
#   print("The youngest child is " + kids[2]+kids[1]+ kids[0])
#
# my_function("Emil", "Tobias", "Linus")




# def my_function(fname, lname):
#   print(fname + " " + lname)
#
# my_function("Email","por po")