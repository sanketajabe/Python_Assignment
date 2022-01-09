s=input("Enter string:")
l=int(len(s)/2)
s1=s[:l]
s2=s[l:]
if(s1==s2):
    print("string is symmetrical")
else:
    print("string is not symmetrical")

rev=s[::-1]
if(s==rev):
    print("string is palindrome")
else:
    print("string is not palindrome")


#output:
    #Enter string:khokho
    #string is symmetrical
    #string is not palindrome

    #Enter string:madam
    #string is not symmetrical
    #string is palindrome
