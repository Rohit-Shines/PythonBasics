# https://www.geeksforgeeks.org/how-to-import-variables-from-another-file-in-python/

# calval.py file where to import variables
# import swaps.py file from which variables
# to be imported
# swaps.py and calval.py files should be in
# same directory.
import file1

# Import x and y variables using
# file_name.variable_name notation
new_x = file1.x
new_y = file1.y

print("x value: ", new_x, "y value:", new_y)

# # Similarly, import swapVal method from swaps file
# x , y = file1.swapVal(new_x,new_y)
#
# print("x value: ", x, "y value:", y)
