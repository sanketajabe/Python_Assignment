#python program to check year is leap or not..

y=int(input('enter year:'))
if(y%4==0 or y%400==0 and y%100!=0):
    print('year is leap')
else:
    print('year is not leap')

#enter year:2016
#year is leap
