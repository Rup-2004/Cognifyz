##Task: Email Validator
##
##Develop a Python function that validates
##whether a given string is a valid email
##address. Implement checks for the format,
##including the presence of an "@" symbol and
##a domain name

def email_checker(a):
    n=len(a)
    if a[n-10]!='@':
        print("Not A Valid Email Address.\n@ Isnot Present.")
        return
    p=ord(a[0])
    if a[0]=="@" or (p>=48 and p<=57):
        print("No Domain name present or wrong domain name...")
        return
    else:
        flag=0
        for i in range(0,n-10):
            p=ord(a[i])
            if not((p>=48 and p<=57)or(p>=48 and p<=57)or (p>=61 and p<=122)):
                flag=1

        if flag==0:
            print("Domain name is ok.")
            return
        else:
            print("Domain name is wrong.")
            return
            

    
x=str(input("Email address:-"))
email_checker(x)
