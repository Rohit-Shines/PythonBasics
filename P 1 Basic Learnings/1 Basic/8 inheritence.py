##Create class and subclass and inherit parent class methods from subclass
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass

#Use the Student class to create an object, and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname()