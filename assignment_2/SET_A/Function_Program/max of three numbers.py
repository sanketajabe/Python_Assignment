def max(a,b,c):
    if(a>b and a>c):
        print(f"{a} is max")
    elif(b>a and b>c):
        print(f"{b} is max")
    else:
        print(f"{c} is max")

a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
max(a,b,c)

#output:
#enter value of a:12
#enter value of b:7
#enter value of c:23
#23 is max
