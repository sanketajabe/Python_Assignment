s=input("Enter String:")
print("original string=",s)
newstr=" "
pos=int(input("enter the position to remove character:"))
for i in range(len(s)):
    if(i!=pos):
        newstr=newstr+s[i]
print("after removal character string=",newstr)


#output:
#Enter String:rbnb colleges
# noriginal string= rbnb colleges
#enter the position to remove character:12
#after removal character string=  rbnb college
