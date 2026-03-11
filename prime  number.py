#wap to prime print number series between 1 to 50

print("1,2",end='')

for x in range(3,50):
    for i in range(2,x):
        if x%i==0:
            break
        else:
            print(x,end='\n')
        
