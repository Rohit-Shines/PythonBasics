# Method 1
a=str(input("Enter the name of the file with .txt extension:"))

# open is a function to open, r is the argument to read the file

file2=open(a,'r')
line=file2.readline()
while(line!=""):
    print(line)
    line=file2.readline()
file2.close()

# Method 2
###### Another simple Code to give file namde directly

f = open("read","r")
print(f.read())
f.close()