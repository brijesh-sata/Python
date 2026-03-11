#WAP for print sum of n natural numbers.
n=int(input("Enter the Natural Number:="))
total=0
for i in range(1,n+1):
    total =total+i**2
print("Sum of First",n,"Natural Number is:",total)
