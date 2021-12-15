#write a python program to find armstrong number in an interval
a=int(input('enter stating number:'))
b=int(input('enter ending number:'))
for i in range(a,b):
    n=i
    s=0
    while(n>0):
        d=n%10
        n=int(n/10)
        s=s+(d*d*d)
    if(s==i):
        print(i)

#enter stating number:100
#enter ending number:1000
#153
#370
#371
#407
