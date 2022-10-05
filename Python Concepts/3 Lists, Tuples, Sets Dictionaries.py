# LIST [] , Ordered, Changeable, Allow Duplicate values, any data type  ## Slow
# TUPLES () , Ordered , Unchangeable , Allow Duplicate                  ## Faster
# SET {} , Unordered , Unchangeable, No Duplicates, No index            ## Fastest   Set items are unchangeable, but you can remove items and add new items.
# DICTIONARY , ordered, Changeable , No duplicates

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

thislist = ["apple", "banana", "cherry", "cat", "dog"]
print(thislist);
print(len(thislist)) # 5
print(type(thislist)) #  <class 'list'>
print(thislist[1]) # banana
print(thislist[2:5]); # means 2 to 4 ['cherry', 'cat', 'dog']
print(thislist[:4]) ; # means 1 - 3 ['apple', 'banana', 'cherry', 'cat']
print(thislist[2:]); # means 2 to end ['cherry', 'cat', 'dog']

# Check if list exists
if "apple" in thislist: print("Yes")

# Change list
thislist[1] = "blackcurrant"
thislist[1:3] = ["blackcurrant", "watermelon"]

####### Tuple #########
thistuple = ("apple", "banana", "cherry") ;print(thistuple)

#### Sets ######
myset = {"apple", "banana", "cherry"}; print(myset)

### Dictionary ###
thisdict = {"brand": "Ford","model": "Mustang","year": 1964} ;print(thisdict)

# Changing and adding Dictionary Elements
my_dict = {'name': 'Jack', 'age': 26}
my_dict['age'] = 27 #Output: {'age': 27, 'name': 'Jack'}
my_dict['address'] = 'Downtown' # Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
