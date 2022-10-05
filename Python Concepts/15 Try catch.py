# import module sys to get the type of exception
try - WHhen error occurs it will execute Content in the Except statement
if - whe error occues it is errored out

import sys
list = ['a', 0, 2]

for i in list:
    try:
        print("The entry is", i)
        r = 1/int(i)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)