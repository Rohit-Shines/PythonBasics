# R- Read/ W- Writwe / A- Append / X- Create/ F- Format/ T- text mode / B -Binary mode

################ Read existing file #################
# open file in same location
# o = open("apple.txt", "r") # open file / r is read
# r = o.read() # read
# print(r)
#
# # open file in different Location
# f = open("/Users/rohitkumargundu/Documents/GitHub/Leet Code Shines/Sorting Algotihms/apple.txt", "r")
# print(f.read())
#
# # read only starting characters of file
# print(open("apple.txt","r").read(6))
#
#
# # reading only first line
# print(open("apple.txt","r").readline())

################ Write to existing file #################

# Write
# a = open("apple.txt", "a") ; a.write(" adding few more lines"); a.close() # a is append here
# a = open("apple.txt", "r") ;print(a.read())

################ over wright  to existing file #################

# Write
# a = open("apple.txt", "w") ; a.write(" adding few more lines"); a.close() # a is append here
# a = open("apple.txt", "r") ;print(a.read())


## create
# f = open("myfile.txt", "x") # creates the file in same folder as the script
# f = open("myfile.txt", "w") #Create a new file if it does not exist:

## Delete file
# import os
# os.remove("apple.txt")


## check if file exists
import os
os.remove("file")

# removing a folder
os.rmdir("directory path")