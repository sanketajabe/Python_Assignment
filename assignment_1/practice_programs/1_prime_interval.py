#python program to print all numbers in an interval..

a=int(input('enter limit 1:'))
b=int(input('enter limit 2:'))
for n in range(a,b):
    f=0
    for i in range(2,n):
        if(n%i==0):
            f=1
            break
    if(f==0):
          print(n)

#enter limit 1:10
#enter limit 2:30
#11
#13
#17
#19
#23
#29
