
names = ["Rose", "Max", "Nina", "Phillip"]

### break # The break statement will completely break out of the current loop,
for i in names:
    print(i)
    if i == "Nina":
        break
    # Hello, Rose
    # Hello, Max
    # Hello, Nina

### Continue ### continue works a little differently. Instead, it goes back to the start of the loop, skipping over any other statements contained within the loop.
for i in names:
    if i != "Nina":
        continue
    print(names)
# ['Rose', 'Max', 'Nina', 'Phillip']


###### Return ##### this will exit from complete definition // break = exit for loop , Return =
for name in names:
        print(name)
        if name == "Nina":
            print("apple")
    return "Found the special name"
