
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

for i in numbers: print(i) # , 6, 5, 3, 8, 4, 2, 5, 4, 1

for i in range(len(numbers)): print(i) # 0,1,2....N
for x in range(2, 30, 3): print(x) # start 2, stop 30, step 3 // 2, 5, 8

# Multin for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits: print(x, y)

# for loop with else
for i in numbers: print(i)
else: print("No items left.")
# 6, 5, 3, 8, 4, 2, 5, 4, 11    and no items left


