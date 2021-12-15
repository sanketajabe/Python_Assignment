#write a python program to print the fabonacci sequence..
a=0
b=1
print('fibonacci sequence=',a,b,end='')
for i in range(1,10):
    c=a+b
    print(c,end='')
    a=b
    b=c

#fibonacci sequence= 0 11235813213455
