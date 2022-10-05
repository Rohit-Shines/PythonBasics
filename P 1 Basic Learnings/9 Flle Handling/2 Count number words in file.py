FileName = input("Enter file name: ")

num_words = 0   # Declaring Variable word count to 0
num_lines = 0   # Declaring Variable word line count to 0

with open(FileName, 'r') as f:
    for line in f:  # For each line
        num_lines += 1
        words = line.split()  # Split a string into a list where each word counts to 1
        num_words += len(words)
        
print("Number of words:")
print(num_words)
print("Number of Lines:")
print(num_lines)

#### Example ###
# txt = "welcome to the jungle"
#
# x = txt.split()
#
# print(x)
#
#
# o/p =  ['welcome', 'to', 'the', 'jungle']