# The next() function returns the next itemBox in an iterator.
mylist = iter(["apple", "banana", "cherry"])
print(next(mylist)) # apple
print(next(mylist)) # banana
print(next(mylist)) # cherry

# different usage of next
random = [5, 9, 'cat']

# converting the list to an iterator
random_iterator = iter(random) ;
print(random_iterator) # 5
print(next(random_iterator)) # 9
print(next(random_iterator))# cat
