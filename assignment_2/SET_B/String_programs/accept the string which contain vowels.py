s=input("enter string:")
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in vowels:
    if i not in s:
        print(f"{s} is accepted")
        break
    else:
        print(f"{s} is not accepted")
        break
#output:
#enter string:AEiouAAIOUeeeIOUA
#AEiouAAIOUeeeIOUA is accepted

