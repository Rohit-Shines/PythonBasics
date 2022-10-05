# #The try block lets you test a block of code for errors.
# #The except block lets you handle the error.
# #The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
  print(z)
except:
  print("An exception occurred")

##Since the try block raises an error, the except block will be executed.
## Without the try block, the program will crash and raise an error:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")



# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")