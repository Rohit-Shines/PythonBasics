# Python3 program introducing f-string

# Ex 1
val = 'Geeks'
print(val,"for",val) # Norma method -> Geeks for Geeks
print(f"{val} for {val}") # f string method  -> Geeks for Geeks\
f"Your answer is "{val}""

# Ex-2
name = 'Tushar' ;age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")



# Prints today's date with help of datetime library
import datetime;
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}") # August 18, 2022

