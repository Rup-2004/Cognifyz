
##Task: String Reversal
##Create a Python function that takes a
##string as input and returns the reverse of
##that string. For example, if the input is
##"hello", the function should return "olleh".





def reversefunc(a):
    return a[::-1]


try:
    x=str(input("Enter the string="))
    print("The reverse string=",reversefunc(x))
except:
    print("Wrong Input")
