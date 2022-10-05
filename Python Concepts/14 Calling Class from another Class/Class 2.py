# importing all the
# functions defined in test.py

import Class1

obj=Class1.Display()

obj.displayText(2,3) # Public so executed
obj._displayText2() # protected but imported so executed
obj.__displayText3() # Private  so not executed





