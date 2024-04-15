##Task: Fibonacci Sequence
##
##Write a Python function that generates the
##Fibonacci sequence up to a given number of
##terms. The function should take an integer
##input from the user and display the
##Fibonacci sequence up to that number of
##terms.


def fibonacci():
    f0=0
    f1=1
    n=int(input("number of terms:"))
    print("\nInitial:0\n\nInitial:1")
    for i in range(0,n):
        f2=f0+f1
        f0=f1
        f1=f2
        print("\n",i+1,".",f2)


fibonacci()
        

