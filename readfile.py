"""Write a program to read a file and display its contents. At the end it shall
also display no. of words available in file."""

file = open("abc.txt","r")

data = file.read()

print("File Content:\n")
print(data)

words=data.split()
count=len(words)

print("\n Total Numbers of Words in File:",count)

file.close()
