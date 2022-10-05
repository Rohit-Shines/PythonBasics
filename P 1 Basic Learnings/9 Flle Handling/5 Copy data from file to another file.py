
# M1
# copy the data
File1 = input("Enter file name to be copied data from ")
File2 = input("Enter file name where data to be copied")


with open(File1) as f:
    with open(File2, "w") as f1:
        for line in f:
            f1.write(line)

#M2
# Append the data already exited data
File1 = input("Enter file to be read from: ")
File2 = input("Enter file to be appended to: ")
fin = open(File1, "r")
data2 = fin.read()
fin.close()
fout = open(File2, "a")
fout.write(data2)
fout.close()