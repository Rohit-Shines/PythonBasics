# All classes have a function called __init__(), which is always executed when the class is being initiated.

##############   Parent classs ##############
class Person:
  def __init__(self, fname, age): # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
    self.name_mowa = fname #  name is assigned with value name_mowa to be called
    self.age_mowa = age

  def printname(abc): # here self can be called with any name
    print("Hello my name is " + abc.name_mowa)# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# p1 = Person("John", 36)
# p1.printname()

######### Child class and how to call its methods and functions ######

class Student(Person): # this is Child class intherting the properties of parent class "Person"
    # pass # is given to avoid any errors when there is nothing inside class
    def __init__(self, fname, age,year): # year extra is added
        Person.__init__(self, fname, age) # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
        super().__init__(fname, age) # super() function that will make the child class inherit all the methods and properties from its parent:
        self.graduationyear= year # variable belongs to this child class only

    def welcome(self):
        print("Welcome", self.name_mowa, self.age_mowa, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2015) # this will use methods from parent and child class
x.welcome()
