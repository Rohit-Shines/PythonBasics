# Index  // list.index(element, start, end)
# Count // Count of the value number of times // list.count(element)

# Append // Add to end of list // list.append(elem)
# Insert // Insert in specific place // list.insert(i, elem)
# Extend // add another list, tuple string // list1.extend(list2)
# copy // copy to another list// list 2= list1.copy()

# POP // Removes itemBox in list //  list.pop(index)
# Remove // Remove first matching element // list.remove(element)
# clear // Emtys the list // list.clear()

# Reverse // Reverse the element with value // list.reverse()  // ( another method list[start:stop:step] )
# sort // ascend and descend // list.sort() and  list.sort(reverse=True)


# The index() method returns the index of the specified element in the list.
# The append() method adds an itemBox to the end of the list.
# The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
# The insert() method inserts an element to the list at the specified index.
# The remove() method removes the first matching element (which is passed as an argument) from the list
# The count() method returns the number of times the specified element appears in the list.
# The pop() method removes the itemBox at the given index from the list and returns the removed itemBox.
# The reverse() method reverses the elements of the list
#The sort() method sorts the items of a list in ascending or descending order.
# The copy() method returns a shallow copy of the list.
# The clear() method removes all items from the list.

# get the index of 'ball'd
animals = ['apple', 'ball', 'cat ', 'dog']
index = animals.index('ball') ;print(index)
# Output: 1

# Index error
# index = animals.index('anaconda') ;print(index) # ValueError: 'anaconda' is not in list

###### Count #######
c = animals.count("apple");print(c) # 1

########## Append     ######
# append 'Yen' to the list
animals.append('elephant'); print(animals)
# Output: ['Dollar', 'Euro', 'Pound', 'Yen']

#### Extend #####
fruits=["mango", "cherry"] ; animals .extend(fruits); print(animals)
# ['apple', 'ball', 'cat ', 'dog', 'elephant', 'mango', 'cherry']

### insert ####
animals.insert(0, "eagle"); print(animals) # ['eagle', 'apple', 'ball', 'cat ', 'dog', 'elephant', 'mango', 'cherry']

### Remove####
animals.remove("eagle"); print(animals) # ['apple', 'ball', 'cat ', 'dog', 'elephant', 'mango', 'cherry']

## pop    #####
prime_numbers = [2, 3, 5, 7]
removed_element = prime_numbers.pop(2) # remove the element at index 2
print(prime_numbers) # Removed 5
print(removed_element)# popped value 5
#[2, 3, 7]
# 5

print('pop Value:', prime_numbers.pop(-1)) # 7

####### Reverse ######
prime_numbers.reverse()
print("Reversed", prime_numbers)

# Syntax: reversed_list = systems[start:stop:step]
systems = [1,2,3,4,5,6,7]; reversed_list = systems[::-1] ;print('Updated List:', reversed_list)
# Updated List: [7, 6, 5, 4, 3, 2, 1]
reversed_list = systems[::-2] ;print('Updated List:', reversed_list)
# Updated List: [7, 5, 3, 1]


##### Sort ###
prime_numbers = [11, 3, 7, 5, 2]
prime_numbers.sort(); print(prime_numbers) # [2, 3, 5, 7, 11]

# Sort the list in Descending order
prime_numbers.sort(reverse=True); print(prime_numbers) # [11, 7, 5, 3, 2]

#  Sort the list using key
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# random.sort(key=0) #


##### Copy ###### The copy() method returns a new list. It doesn't modify the original list.
copied= prime_numbers.copy(); print(copied) # [11, 7, 5, 3, 2]

###### CLear ###### The clear() method removes all items from the list.
Cleared= prime_numbers.clear; print(Cleared) # <built-in method clear of list object at 0x10895be80>
