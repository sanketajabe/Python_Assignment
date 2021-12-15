#python program to check the number is armstrong or not..

n=int(input('enter number:'))
temp=n
s=0
while(n>0):
    d=n%10
    n=int(n/10)
    s=s+(d*d*d)
if(s==temp):
    print('number is armstrong')
else:
    print('number is not armstrong')

#enter number:153
#number is armstrong
