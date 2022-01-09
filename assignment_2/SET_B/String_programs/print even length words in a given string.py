s=input("enter string:")
s=s.split(' ')
print(s)
print("even length words:")
for i in s:
    if(len(i)%2==0):
        print(i)

#output:
#enter string:rbnb college shrirampur
#['rbnb', 'college', 'shrirampur']
#even length words:
#rbnb
#shrirampur
