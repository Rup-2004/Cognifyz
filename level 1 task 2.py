##Task: Temperature Conversion
##
##Create a Python program that converts
##temperatures between Celsius and
##Fahrenheit. Prompt the user to enter a
##temperature value and the unit of
##measurement, and then display the
##converted temperature.

def tempconvertion(a):
    try:
        n=len(a)
        if a[n-1]=='C' or a[n-1]=='c':
            c=float(a[0:n-1])
            f=float((9/5)*c+32)
            print(c," C -> ",f," F")
        
        if a[n-1]=='F' or a[n-1]=='f':
            f=float(a[0:n-1])
            c=float((5/9)*(f-32))
            print(f," F -> ",c," C")

    except:
        print("Wrong Input.")    




x=str(input('Temperature (FORMAT:- 100C,32F)='))
tempconvertion(x)
