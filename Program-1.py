#WAP for print the fabonacci series.
num=int(input("Enter the number:"))
a,b=0,1

print("Febonacci Series:=")
for _ in range(num):
    print(a,end='\n')
    a,b=b,a+b
