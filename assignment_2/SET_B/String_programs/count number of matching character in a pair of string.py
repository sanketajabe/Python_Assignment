s1=input("enter string 1:")
s2=input("enter string 2:")
c1=0
for i in range(len(s1)):
    for j in range(len(s2)):
        if(s1[i]==s2[j]):
            c1=c1+1
            break
print("no of matching character=",c1)

#output:
#enter string 1:sanket
#enter string 2:ajabe
#no of matching character= 2
