#Write a program to execute user defined exception in python.

x=int(input("Enter the Value:="))
try:
    if x<0:
        raise Exception
    else:
        print("It's Valid")
except:
    print("Error")
