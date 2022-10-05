# simple use iter instead of for loop
# __iter__() and __next__() - > An iterator is an object that can be iterated upon, meaning that you can traverse through all the values

##### __iter__() and __next__() #####
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit)); print(next(myit)) ; print(next(myit)) # apple banana cherry

#### string with iter ######
name ="apple"
a=iter(name)
print(next(a));print(next(a));print(next(a));print(next(a));print(next(a));

###

