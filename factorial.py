#wap to print the factorial of given number

n=int(input("Enter the Number:-"))

fact=1
for i in range(1,n+1):
    fact*=i
    print("Factorial of",n,"is",fact)
