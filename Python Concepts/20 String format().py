# The format() method allows you to format selected parts of a string.

a = 49
b = "The price is {} dollars"
print(b.format(a)) # The price is 49 dollars

c ="The price is {:.2f} dollars"
print(c.format(a)) #The price is 49.00 dollars

### Print multiple values using format()
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of itemBox number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price)) # I want 3 pieces of itemBox number 567 for 49.00 dollars.

### if you want to refer to the same value more than once, use the index number:
apple = "I want {0} pieces of itemBox number {0} for {1} dollars."
print(apple.format(quantity, itemno ))
