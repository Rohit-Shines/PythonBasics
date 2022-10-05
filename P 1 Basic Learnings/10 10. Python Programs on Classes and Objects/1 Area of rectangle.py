

class rectangle():
    #__init__ method is similar to constructors in C++ and Java . Constructors are used to initialize the object's state
    #__init__ is like a constructer and called automatically and run.
    def __init__(self, breadth, length):   # SELF IS Aa object created to invoke all the arguments to call again
        self.breadth = breadth
        self.length = length

    def area(self):     # self is called instead of breadth and lenghth here
        return self.breadth * self.length


a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))

print("Area of rectangle:", rectangle(a, b) .area())  # Calling class and function in it

print()