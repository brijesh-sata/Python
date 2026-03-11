#Write a program to generate arithmetic exception and log the exception in system.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result= a/b
    print("Result:=",result)
except ZeroDivisionError:
    print("Division is not Possible.")
    
