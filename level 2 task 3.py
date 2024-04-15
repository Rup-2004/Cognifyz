##Task: Password Strength Checker
##
##Create a Python function that evaluates
##the strength of a password entered by the
##user. Implement checks for factors such as
##length, presence of uppercase and
##lowercase letters, digits, and special
##characters.


def strength_checker():
    flagout=0
    while flagout==0:
        a=str(input("\nEnter the password:-"))
        if len(a)<8:# it is to check the length ,password must be 8 or greater than that
            print("\nToo short password.")
            continue
        flagin=0
        
        for i in range(0,len(a)):
            if(ord(a[i])>=65 and ord(a[i])<=90):#here I use ascii values for upper case it is 65 to 90
                flagin=1
                break
        if flagin==0:
            print("\nNo Upper Case letter in password")
            continue
            
        flagin=0
        for i in range(0,len(a)):
            if(ord(a[i])>=97 and ord(a[i])<=122):
                flagin=1
                break
        if flagin==0:
            print("\nNo Lower Case letter in password")
            continue
        
        flagin=0
        for i in range(0,len(a)):
            if(ord(a[i])>=48 and ord(a[i])<=57):
                flagin=1
                break
        if flagin==0:
            print("\nNo Digit in password")
            continue

        flagin=0
        for i in range(0,len(a)):
            if (ord(a[i])>=33 and ord(a[i])<=47) or (ord(a[i])>=58 and ord(a[i])<=64) or (ord(a[i])>=91 and ord(a[i])<=96) or (ord(a[i])>=123 and ord(a[i])<=126):
                flagin=1
                break
        if flagin==0:
            print("\nNo Special Charecter in password")
            continue
    
        flagout=1
    print("\nPassword is strong enough.")


strength_checker()
