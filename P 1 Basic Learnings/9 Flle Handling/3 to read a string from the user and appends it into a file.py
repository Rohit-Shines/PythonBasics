
fname = input("Enter file name: ")
file3=open(fname,"a")   # a stands here to append
c=input("Enter string to append: \n");

# Writing the appended data to file.
file3.write("\n")
file3.write(c)
file3.close()

# Opening the file and printing the data
print("Contents of appended file:");
file4=open(fname,'r')
line1=file4.readline()
while(line1!=""):
    print(line1)
    line1=file4.readline()
file4.close()