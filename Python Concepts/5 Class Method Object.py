
# This will explain different ways to calls def inside class
class Solution:

    def test(self):# you can five any word in place of self  # self helps us to refer this objects to here/ without self we cannot refere
        print("apple")

obj =Solution() # initiating the Object to point to class
obj.test() # Method 1 -> Calling directly
Solution.test(obj) # Method 2 -> calling with argument obj

### The __init__() Function######
# The __init__() function is called automatically every time the class is being used to create a new object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36) # object
print(p1.name); print(p1.age) # John, 36

####Object Methods using self####
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
class Person:
  def __init__(self, name, age):
    self.name = name; self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name) # self.name using details from __init__ Definition

p1 = Person("John", 36)
p1.myfunc()